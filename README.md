# RAG-Chatbot-using-LangChain-Chroma-HuggingFace

A simple Retrieval-Augmented Generation (RAG) chatbot built using open-source tools like LangChain, Chroma (vector DB), and HuggingFace Transformers. This chatbot allows you to ask questions from your own PDF documents.

---

## 📁 Project Structure
"""
rag_chatbot/
├── main.py # Main script to run the chatbot
├── load_documents.py # Loads PDF/TXT documents
├── vector_store.py # Creates vector store using Chroma
├── rag_chatbot.py # Defines the chatbot logic
├── requirements.txt # List of dependencies
├── Upload your file # Sample document (or your own)
└── chroma_db/ # Chroma's persistent DB files (auto-created)
"""

---

## ⚙️ Features

- 🔍 Load and read your own PDF or TXT documents.
- 🤖 Ask natural language questions about the document.
- 🧠 Uses sentence-transformer (`all-MiniLM-L6-v2`) for embeddings.
- 🧾 Uses `CTransformers` with Mistral 7B GGUF model for local inference.

---

## 🚀 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/Ali-619/RAG-Chatbot-using-LangChain-Chroma-HuggingFace.git
cd RAG-Chatbot-using-LangChain-Chroma-HuggingFace

**2. Create & Activate Virtual Environment**

python -m venv venv
.\venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt

4. Add Your Document

update the path in main.py:

file_path = r"C:\Users\yourname\Desktop\rag_chatbot\yourfile.pdf"

 Run the Chatbot

python main.py

