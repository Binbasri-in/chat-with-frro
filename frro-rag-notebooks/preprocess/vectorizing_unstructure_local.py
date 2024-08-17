import os
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import dict_to_elements
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Define the path to the directory containing PDF files
path_to_pdfs = "examples/data/"

# Function to process a single PDF file
def process_pdf(path_to_pdf):
    elements = partition_pdf(path_to_pdf, chunking_strategy="by_title", max_characters=512, languages=["eng", "hin"])
    print(f"Processed {path_to_pdf}")
    return elements

# Process all PDF files in the directory
all_elements = []
for filename in os.listdir(path_to_pdfs):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(path_to_pdfs, filename)
        elements = process_pdf(pdf_path)
        all_elements.extend(elements)
        
# Convert elements to Langchain Documents
documents = []
for element in all_elements:
    metadata = element.metadata.to_dict()
    documents.append(Document(page_content=element.text, metadata=metadata))
    
# Create FAISS vector store from documents
db = FAISS.from_documents(documents, HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5"))
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

db.save_local("data/faiss_db_local")

