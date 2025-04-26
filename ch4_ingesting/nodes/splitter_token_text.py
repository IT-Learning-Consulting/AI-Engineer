"""
This script demonstrates how to use LlamaIndex's TokenTextSplitter to process a local text file,
splitting the text into chunks based on token count while configuring a global LLM model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Reading a Markdown file using FlatReader.
- Splitting the document into token-based chunks using TokenTextSplitter, with primary and backup separators.
- Printing each node's text, metadata, index, and text length.

Useful for preparing documents for fine-grained token-based processing such as embedding generation,
indexing, or fine-tuned querying.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from pathlib import Path
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.readers.file import FlatReader


# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

document = reader.load_data(Path("../files/documents/the_empire.md"))

splitter = TokenTextSplitter(
    chunk_size=70, chunk_overlap=2, separator=" ", backup_separators=[".", "!", "?"]
)

nodes = splitter.get_nodes_from_documents(document)
for index, node in enumerate(nodes):
    print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
    print(f"LENGTH: {len(node.text)}\n")
