"""
This script demonstrates how to use LlamaParse with LlamaIndex to extract text from PDFs and create a vector-based
searchable index using a language model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Using LlamaParse as a custom file extractor for PDF files.
- Reading and parsing a specific PDF file.
- Creating a VectorStoreIndex from the parsed document.
- Querying the index with a natural language question.

Useful for building a lightweight semantic search engine or Q&A system over PDF content, such as rulebooks,
manuals, or documentation.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_parse import LlamaParse


# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

parser = LlamaParse(result_type="text")

file_extractor = {".pdf": parser}
reader = SimpleDirectoryReader(
    input_files=["files/documents/llama_parse_pdf_test.pdf"],
    file_extractor=file_extractor,
)

doc = reader.load_data()

index = VectorStoreIndex(doc)
qe = index.as_query_engine()
response = qe.query("What are the talents of an Empire Crossbowman?")
print(response)
