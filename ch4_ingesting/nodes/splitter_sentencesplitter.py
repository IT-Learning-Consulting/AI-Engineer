"""
This script demonstrates how to use LlamaIndex's FlatReader and SentenceSplitter to process a local text file
and split it into smaller nodes for downstream tasks, while configuring a global LLM model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Reading a Markdown file using FlatReader.
- Splitting the document into small chunks (nodes) using SentenceSplitter with a defined chunk size and no overlap.
- Printing each node's text, metadata, and its index.

Useful for preparing structured and manageable document pieces for indexing, training, or fine-grained querying.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import FlatReader
from pathlib import Path
from llama_index.llms.openai import OpenAI

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

document = reader.load_data(Path("../files/documents/the_empire.md"))

splitter = SentenceSplitter(chunk_size=50, chunk_overlap=0)
nodes = splitter.get_nodes_from_documents(document)
for index, node in enumerate(nodes):
    print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
