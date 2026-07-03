import os
from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    TextLoader,
    DirectoryLoader,
    Docx2txtLoader
)


PDF_FOLDER = "data/pdfs"
DOC_FOLDER = "data/docs"
TXT_FOLDER = "data/txt"


def load_documents():

    documents = []

    # PDF
    if os.path.exists(PDF_FOLDER):
        pdf_loader = PyPDFDirectoryLoader(PDF_FOLDER)
        documents.extend(pdf_loader.load())

    # DOCX
    if os.path.exists(DOC_FOLDER):
        doc_loader = DirectoryLoader(
            DOC_FOLDER,
            glob="*.docx",
            loader_cls=Docx2txtLoader
        )
        documents.extend(doc_loader.load())

    # TXT
    if os.path.exists(TXT_FOLDER):
        txt_loader = DirectoryLoader(
            TXT_FOLDER,
            glob="*.txt",
            loader_cls=TextLoader
        )
        documents.extend(txt_loader.load())

    return documents