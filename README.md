```markdown
# Naval RAG Chatbot  
A Retrieval-Augmented Generation system that answers questions using Naval Ravikant's wisdom from podcasts and writings. Combines semantic search with LLM generation for context-aware philosophical responses.

![Tech Stack](https://img.shields.io/badge/Powered_By-Pinecone-430098?logo=pinecone&style=flat)
![License](https://img.shields.io/badge/License-MIT-blue)

## Features  
- **Philosophical Q&A**: Answers in Naval's signature style using 1000+ knowledge chunks  
- **Vector Search**: Pinecone-powered semantic retrieval with cosine similarity  
- **Streamlined UI**: Simple web interface with source attribution  
- **API First**: FastAPI backend with Swagger documentation  
- **Efficient Chunking**: LangChain text splitting with context preservation  

## Project Structure  
```
├── data_prep.py              # Data processing & Pinecone upsert
├── main.py                   # FastAPI server & core logic
├── frontend.html             # Chat interface (HTML/JS)
├── naval_data.json           # Processed transcripts
├── .env.example              # Environment template
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Installation  
1. **Clone Repository**  
```
git clone https://github.com/yourusername/naval-rag-chatbot.git
cd naval-rag-chatbot
```

2. **Set Up Environment**  
```
python -m venv naval_rag_env
source naval_rag_env/bin/activate  # Linux/Mac
# .\naval_rag_env\Scripts\activate  # Windows
```

3. **Install Dependencies**  
```
pip install -r requirements.txt
```

4. **Configure API Keys**  
Create `.env` file:  
```
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=us-east-1
GOOGLE_API_KEY=your_gemini_key
```

## Data Preparation  
Process and upload transcripts to Pinecone:  
```
python data_prep.py
```
*Processes ~1000-character chunks with 200-character overlap using LangChain's RecursiveTextSplitter*

## Usage  
**Start API Server**  
```
python main.py
```

**Access Endpoints**  
| Endpoint | Method | Description |  
|----------|--------|-------------|  
| `/ask`   | POST   | Submit questions (JSON: `{"text": "your question"}`) |  
| `/health`| GET    | System status check |  
| `/docs`  | GET    | Interactive API documentation |  

**Chat Interface**  
Visit `http://localhost:8000/chat`  

## Tech Stack  
Component | Technology  
---------|-----------  
Backend | FastAPI  
Embeddings | SentenceTransformers (all-MiniLM-L6-v2)  
Vector DB | Pinecone (Serverless)  
LLM | Google Gemini API  
Chunking | LangChain Text Splitter  
Frontend | HTML/JS  

## Example Queries  
- "How does Naval define wealth?"  
- "What's the difference between specific and general knowledge?"  
- "How to find peace in modern life?"  

## Configuration  
**Pinecone Index Settings**  
```
{
  "dimension": 384,
  "metric": "cosine",
  "pod_type": "starter"
}
```

**Environment Requirements**  
- Python 3.10+  
- Free Pinecone account  
- Google Gemini API access  

## License  
MIT License - Free for non-commercial use

## Future Roadmap
- Add streaming responses
- Implement chat history
- Enhance UI with React/Tailwind
- Add rate limiting
```

Simply copy-paste this into your `README.md` file. The Markdown formatting includes proper code blocks, tables, and structure for optimal GitHub rendering. Contains all essential sections with precise technical details matching your actual codebase.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/52032377/cb8ae567-e6bb-4c9d-b1f5-8ee3ac4dd666/paste.txt

---
Answer from Perplexity: pplx.ai/share
