"""
This script demonstrates how to use LlamaIndex's HierarchicalNodeParser to process a text document
by creating multiple levels of nodes with different chunk sizes, while configuring a global LLM model.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Reading a Markdown file using FlatReader.
- Defining a HierarchicalNodeParser with multiple SimpleNodeParsers at different chunk sizes (128, 64, 32).
- Parsing the document into nodes with associated metadata.
- Printing each node's metadata, index, and text length.
- Saving all parsed nodes and their metadata into a text file.

Useful for multi-granularity document indexing, allowing flexible querying across coarse and fine content levels.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from pathlib import Path
from llama_index.core import Settings
from llama_index.core.node_parser import HierarchicalNodeParser, SimpleNodeParser
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import FlatReader

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

documents = reader.load_data(Path("../files/documents/the_empire.md"))

parser = HierarchicalNodeParser(
    chunk_sizes=[128, 64, 32],
    node_parser_ids=["128", "64", "32"],  # <-- you were missing this
    node_parser_map={
        "128": SimpleNodeParser(chunk_size=128, chunk_overlap=0),
        "64": SimpleNodeParser(chunk_size=64, chunk_overlap=0),
        "32": SimpleNodeParser(chunk_size=32, chunk_overlap=0),
    },
)

nodes = parser.get_nodes_from_documents(documents)
for index, node in enumerate(nodes):
    # print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
    print(f"LENGTH: {len(node.text)}\n")

# Save nodes to a txt file
output_path = Path("parsed_nodes.txt")

with open(output_path, "w", encoding="utf-8") as f:
    for index, node in enumerate(nodes):
        f.write(f"Node {index}:\n")
        f.write(node.text + "\n")
        f.write(str(node.metadata) + "\n")
        f.write(f"LENGTH: {len(node.text)}\n")
        f.write("\n" + "-" * 50 + "\n\n")

print(f"Saved {len(nodes)} nodes to {output_path}")
