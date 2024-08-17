import os
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
from unstructured.staging.base import dict_to_elements
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub.hf_api import HfFolder
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Set your environment variables and API keys
os.environ["UNSTRUCTURED_API_KEY"] = "<YOUR_UNSTRUCT_API_KEY>"
unstructured_api_key = os.environ.get("UNSTRUCTURED_API_KEY")

# Initialize Unstructured Client
client = UnstructuredClient(api_key_auth=unstructured_api_key)

# Define the path to the directory containing PDF files
path_to_pdfs = "examples/data/"

# Function to process a single PDF file
def process_pdf(path_to_pdf):
    with open(path_to_pdf, "rb") as f:
        files = shared.Files(content=f.read(), file_name=path_to_pdf)
        req = shared.PartitionParameters(files=files, chunking_strategy="by_title", max_characters=512)
        try:
            resp = client.general.partition(req)
            elements = dict_to_elements(resp.elements)
            return elements
        except SDKError as e:
            print(e)
            return []

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

db.save_local("data/faiss_db_api")
