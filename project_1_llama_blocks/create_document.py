"""
Create a Llama document manually
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
