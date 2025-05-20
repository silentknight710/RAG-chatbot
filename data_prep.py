from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import JSONLoader
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from tqdm import tqdm  # For progress bars

# Load environment variables
load_dotenv(dotenv_path='.env', encoding='utf-8')

# 1. Load JSON data
loader = JSONLoader(
    file_path="naval_data.json",
    jq_schema=".[].transcript[]",
    text_content=False
)
documents = loader.load()

# 2. Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Split into 1000-character chunks
    chunk_overlap=200  # Overlap to avoid losing context
)
chunks = text_splitter.split_documents(documents)

# 3. Initialize embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 4. Initialize Pinecone connection
pc = Pinecone(
    api_key='pcsk_6CkPhv_7SUQRC2XNccCyxha7AwXn7uc8hvAyAaSCtMzdggjJvLNAwZtqr3mkWBs5UBNND6'
             )

# 5. Create or connect to index
index_name = 'naval-rag'
dimension = 384  # Must match all-MiniLM-L6-v2 embeddings

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric='cosine',  # Better for semantic similarity
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

index = pc.Index(index_name)

# 6. Process and upsert in batches
batch_size = 100  # Adjust based on your needs
vectors = []

for i, chunk in enumerate(tqdm(chunks, desc="Processing chunks")):
    vectors.append((
        f"vec_{i}",  # Unique ID
        model.encode(chunk.page_content).tolist(),
        {"text": chunk.page_content}
    ))
    
    # Upsert in batches
    if len(vectors) >= batch_size:
        index.upsert(vectors=vectors)
        vectors = []  # Reset batch

# Upsert any remaining vectors
if vectors:
    index.upsert(vectors=vectors)

print(f"✅ Successfully upserted {len(chunks)} chunks to index '{index_name}'")
print(index.describe_index_stats())  # Verify counts