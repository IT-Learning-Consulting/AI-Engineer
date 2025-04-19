"""
Create a Llama document by importing a wikipedia article
"""

from llama_index.readers.wikipedia import WikipediaReader

# Example 1
loader = WikipediaReader()
documents = loader.load_data(pages=["Pythagorean theorem", "General relativity"])

print(f"loaded {len(documents)} documents")

# Example 2
other_loader = WikipediaReader()
other_document = other_loader.load_data(
    pages=[
        "List of Warhammer Fantasy Roleplay publications",
    ],
    auto_suggest=False,
)

print(other_document)
