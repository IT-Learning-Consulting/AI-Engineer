"""
This script demonstrates how to use LlamaIndex's CodeSplitter to process a Python code file
and split it into manageable chunks, while configuring a global LLM model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Reading a Python file using FlatReader.
- Splitting the code into chunks based on number of lines, overlap, and maximum character limit using CodeSplitter.
- Printing each node's text, metadata, and its index.

Useful for preparing code files for structured indexing, semantic code search, or fine-tuned language model tasks.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from pathlib import Path
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import CodeSplitter
from llama_index.readers.file import FlatReader


# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

document = reader.load_data(Path("./splitter_sentencesplitter.py"))

splitter = CodeSplitter(
    language="python", chunk_lines=5, chunk_lines_overlap=2, max_chars=100
)

nodes = splitter.get_nodes_from_documents(document)
for index, node in enumerate(nodes):
    print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
