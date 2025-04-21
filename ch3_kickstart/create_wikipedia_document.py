"""
This script demonstrates how to create LlamaIndex Document instances by importing Wikipedia articles.

It includes:
- Example 1: Loading multiple Wikipedia pages using auto-suggest.
- Example 2: Loading a specific page without auto-suggest, such as a niche topic.

Useful for testing WikipediaReader's capabilities and preparing documents for indexing.

Author: Danny
Date: 2025-04-19
Version: 1.0
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
