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
```


## Installation  
1. **Clone Repository**  
git clone https://github.com/yourusername/naval-rag-chatbot.git
cd naval-rag-chatbot

