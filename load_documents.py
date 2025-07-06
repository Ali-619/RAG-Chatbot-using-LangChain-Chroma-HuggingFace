from langchain.document_loaders import TextLoader, PDFPlumberLoader

def load_docs(file_path):
    if file_path.endswith(".txt"):
        return TextLoader(file_path).load()
    elif file_path.endswith(".pdf"):
        return PDFPlumberLoader(file_path).load()
    else:
        raise ValueError("Unsupported file type")
