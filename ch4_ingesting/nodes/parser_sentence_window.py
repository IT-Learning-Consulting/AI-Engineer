"""
This script demonstrates how to use LlamaIndex's SentenceWindowNodeParser to process a text document
by creating nodes that include a sliding window of neighboring sentences, while configuring a global LLM model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Reading a Markdown file using FlatReader.
- Splitting the document into sentence windows using SentenceWindowNodeParser, capturing surrounding context.
- Printing each node's text, metadata, index, and text length.

Useful for applications where preserving sentence context improves search relevance, summarization, or retrieval performance.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from pathlib import Path
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.readers.file import FlatReader
from llama_index.llms.openai import OpenAI

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

document = reader.load_data(Path("../files/documents/the_empire.md"))

parser = SentenceWindowNodeParser(
    window_size=2,
    window_metadata_key="text_window",
    original_text_metadata_key="original_sentence",
)

nodes = parser.get_nodes_from_documents(document)
for index, node in enumerate(nodes):
    print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
    print(f"LENGTH: {len(node.text)}")
