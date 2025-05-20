# Naval RAG Chatbot  
*A Retrieval-Augmented Generation system that answers questions using Naval Ravikant's wisdom*

[![Pinecone](https://img.shields.io/badge/Powered_By-Pinecone-430098?logo=pinecone&style=flat)](https://pinecone.io)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com)

## Features  
- **Philosophical Q&A**: Answers in Naval's signature style using 1000+ knowledge chunks  
- **Semantic Search**: Pinecone-powered vector retrieval with cosine similarity  
- **Streamlined UI**: Web interface with source attribution  
- **Efficient Processing**: LangChain text chunking with context preservation  

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
   git clone https://github.com/your-username/naval-rag-chatbot.git
   cd naval-rag-chatbot
   python -m venv naval_rag_env
   source naval_rag_env/bin/activate   # or .\naval_rag_env\Scripts\activate on Windows
   ```
3. **Set Up Environment**
   ```
   pip install -r requirements.txt
   ```
4. **Set Up API Keys**
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENV=your_pinecone_environment
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```
Refer to ```.env.example``` for structure.

## Index Data
Run the following to process and upload Naval's transcript to Pinecone:
```
 python data_prep.py
```
## Run the App
Start the FastAPI server:
```
python main.py
```

The API will be live at: http://127.0.0.1:8000

API Docs (Swagger UI):
Visit http://127.0.0.1:8000/docs

**Web Chat UI:**
Open http://127.0.0.1:8000/chat


## API Overview
POST /ask
Send a question and receive a Naval-style response with sources.

Request Body:
```
{
  "text": "What is Naval's definition of happiness?"
}
```
Response:
```
{
  "question": "...",
  "answer": "...",
  "sources": [
    {"text": "...", "score": 0.92},
    ...
  ]
}
```
## Tech Stack

| Layer      | Tech Used                                 |
| ---------- | ----------------------------------------- |
| Backend    | FastAPI                                   |
| Embeddings | SentenceTransformers (`all-MiniLM-L6-v2`) |
| Vector DB  | Pinecone                                  |
| LLM        | Google Gemini API                         |
| UI         | HTML + JS (served via FastAPI)            |
| Chunking   | LangChain RecursiveCharacterTextSplitter  |

## Example Prompts
"How can I become wealthy?"

"What does Naval think about finding meaning in life?"

"What is the difference between happiness and pleasure according to Naval?"

## Future Improvements
Add chat history and memory

Stream LLM responses

Improve UI with Tailwind or React

Add error handling and rate limits
