"""
This script demonstrates how to manually create TextNode instances using the LlamaIndex library.

It includes:
- Example 1: Creating nodes by slicing a simple document.
- Example 2: Loading a Wikipedia article and splitting the text into multiple nodes manually.

Useful for understanding how TextNodes relate to Documents and how to prepare custom nodes for indexing.

Author: Danny
Date: 2025-04-19
Version: 1.0
"""

from llama_index.core import Document
from llama_index.core.schema import TextNode
from llama_index.readers.wikipedia import WikipediaReader

# Example 1
doc = Document(text="This is a sample document text")
n1 = TextNode(text=doc.text[:16], doc_id=doc.id_)
n2 = TextNode(text=doc.text[17:], doc_id=doc.id_)

print(n1)
print(n2)

# Example 2
loader = WikipediaReader()
document = loader.load_data(
    pages=["List of Warhammer Fantasy Roleplay publications"],
    auto_suggest=False,
)
doc_text = Document(text=document[0].text)


n3 = TextNode(text=doc_text.text[0:99], doc_id=doc.id_)
n4 = TextNode(text=doc_text.text[100:199], doc_id=doc.id_)
n5 = TextNode(text=doc_text.text[200:299], doc_id=doc.id_)
n6 = TextNode(text=doc_text.text[300:399], doc_id=doc.id_)

print(n3)
print(n4)
print(n5)
print(n6)
