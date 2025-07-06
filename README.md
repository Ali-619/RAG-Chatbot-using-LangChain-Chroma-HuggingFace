# RAG-Chatbot-using-LangChain-Chroma-HuggingFace

A simple Retrieval-Augmented Generation (RAG) chatbot built using open-source tools like LangChain, Chroma (vector DB), and HuggingFace Transformers. This chatbot allows you to ask questions from your own PDF documents.

---

## 📁 Project Structure

rag_chatbot/
├── main.py # Main script to run the chatbot
├── load_documents.py # Loads PDF/TXT documents
├── vector_store.py # Creates vector store using Chroma
├── rag_chatbot.py # Defines the chatbot logic
├── requirements.txt # List of dependencies
├── Upload your file # Sample document (or your own)
└── chroma_db/ # Chroma's persistent DB files (auto-created)
