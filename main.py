from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from typing import List, Dict
import requests

# --- Configuration ---
# Load environment variables (dotenv for local overrides)
load_dotenv(dotenv_path='.env', encoding='utf-8')

# Hardcoded API Keys 
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


# Initialize embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize Pinecone client and index
pc = Pinecone(
    api_key=PINECONE_API_KEY
)
index_name = "naval-rag"
# Create index if it doesn't exist
existing = pc.list_indexes().names()
if index_name not in existing:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_ENV
        )
    )
index = pc.Index(index_name)

# --- FastAPI Setup ---
app = FastAPI(
    title="Naval RAG API",
    description="Retrieve and generate answers from Naval Ravikant's knowledge base"
)

class Query(BaseModel):
    text: str

# --- Core Functions ---
def retrieve_context(query: str, top_k: int = 5) -> List[Dict]:
    """Retrieve relevant chunks from Pinecone"""
    try:
        query_embedding = model.encode(query).tolist()
        results = index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        return [{"text": match.metadata["text"], "score": match.score} for match in results.matches]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retrieval failed: {str(e)}")

def generate_answer(context: List[Dict], question: str) -> str:
    """Generate answer using Gemini HTTP API"""
    try:
        context_str = "\n---\n".join([f"{i+1}. {c['text']}" for i, c in enumerate(context)])
        prompt = f"""
You are answering as Naval Ravikant. Use the context provided below to form a thoughtful, concise, and philosophical response to the user's question. If the context doesn’t cover the topic, say: “I don't have Naval's perspective on this.”

Context:
{context_str}

Question: {question}
"""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [{"parts": [{"text": prompt.strip()}]}]
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

# --- API Endpoints ---
@app.get("/")
def root():
    """Root endpoint welcoming users and redirecting to docs"""
    return {"message": "Welcome to the Naval RAG API! Visit /docs for interactive Swagger UI."}

@app.post("/ask")
async def ask_question(query: Query):
    """
    Endpoint to ask questions and get answers with sources
    Example request body: {"text": "How to build wealth?"}
    """
    context = retrieve_context(query.text)
    answer = generate_answer(context, query.text)
    return {
        "question": query.text,
        "answer": answer,
        "sources": context
    }

@app.get("/health")
async def health_check():
    """Endpoint for health checks"""
    stats = index.describe_index_stats()
    return {"status": "healthy", "index_stats": stats}

from fastapi.responses import HTMLResponse

@app.get("/chat", response_class=HTMLResponse)
def serve_chat_ui():
    with open("frontend.html", "r", encoding="utf-8") as f:
        return f.read()

# --- Main Execution ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
