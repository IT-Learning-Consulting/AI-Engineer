"""
This script demonstrates how to manually create Document instances using the LlamaIndex library.

It includes:
- Example 1: A document with sample text and metadata for general content.
- Example 2: A test document showcasing how to define text, metadata, and an ID manually.
- A document stream (list of Document objects) that can be used for further indexing or processing.

Author(s): Danny
Date: 2025-04-19
Version: 1.0
"""

from llama_index.core import Document

# Example 1
text: str = "The quick brown fox jumps over the lazy dog."

doc = Document(
    text=text, metadata={"author": "John Doe", "category": "others"}, id_="1"
)

print(doc)

# Example 2
other_text: str = "I am testing how to create a manual document in llama"

other_doc = Document(
    text=other_text, metadata={"author": "Danny", "category": "test"}, id_="2"
)

print(other_doc)
