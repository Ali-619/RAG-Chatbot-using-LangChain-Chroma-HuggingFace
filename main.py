from load_documents import load_docs
from vector_store import create_vectorstore
from rag_chatbot import create_chatbot

print("✅ Your main.py is working!")

def main():
    file_path = r"C:\Users\ali61\OneDrive\Desktop\rag_chatbot\ALI RAZA.pdf"
    print("📂 Loading document...")
    docs = load_docs(file_path)

    print("📊 Creating vector store...")
    create_vectorstore(docs)

    print("🤖 Starting chatbot...")
    chatbot = create_chatbot()

    while True:
        question = input("\nYou: ")
        if question.lower() in ['exit', 'quit']:
            break
        answer = chatbot.invoke({"query": question})  # ✅ Correct key
        print("Bot:", answer)

if __name__ == "__main__":
    main()
