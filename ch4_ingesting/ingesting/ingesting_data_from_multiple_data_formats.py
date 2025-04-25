"""
This script demonstrates how to use the LlamaIndex SimpleDirectoryReader to load documents from a local directory or specific files,
while setting a global LLM model for downstream text processing.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Example 1: Loading all documents recursively from a folder.
- Example 2: Loading a specific list of files, including PDFs.

Each document's metadata and content (if applicable) is printed for inspection.

Useful for batch-loading datasets from a local source for tasks such as indexing, summarizing, or building search applications.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from llama_index.core import Settings, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

# Example 1
reader = SimpleDirectoryReader(
    input_dir="files/documents",
    recursive=True,
)

documents = reader.load_data()

for doc in documents:
    print(doc.metadata)

# Example 2
files = [
    "files/documents/2025-OJS013-00036963-en-ts.pdf",
    "files/documents/traps.pdf",
    # "files/documents/ChatGPT Image Apr 15, 2025, 12_34_51 PM.png",
]
reader = SimpleDirectoryReader(input_files=files, recursive=True)

documents = reader.load_data()

for doc in documents:
    print(doc.metadata)
    print(doc.text)
