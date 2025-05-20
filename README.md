# RAG-chatbot
A Retrieval-Augmented Generation (RAG) chatbot that responds to your queries using Naval Ravikant's insights from his talks and interviews. It combines semantic search with LLMs to give thoughtful, context-rich answers.

📁 Project Structure
graphql
Copy
Edit
.
├── __pycache__/                  # Python cache files
├── naval_rag_env/               # Your virtual environment folder
├── .env                         # API keys and secrets
├── .env.example                 # Template for .env
├── data_prep.py                 # Script for chunking and upserting data to Pinecone
├── frontend.html                # Web UI for chat
├── gemini.py                    # Gemini API wrapper and prompt logic
├── get-pip.py                   # Bootstrap pip installer
├── main.py                      # FastAPI backend with endpoints
├── naval_data.json              # Transcript data (source material)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (this file)
🚀 Quick Start
