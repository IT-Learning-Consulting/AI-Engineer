"""
This script demonstrates how to create relationships between TextNode instances using the LlamaIndex schema.

It includes:
- Example: Manually linking two nodes with NEXT and PREVIOUS relationships to reflect logical or sequential flow.

Useful for building custom graphs of node relationships when indexing documents.

Author: Danny
Date: 2025-04-20
Version: 1.0
"""

from llama_index.core import Document
from llama_index.core.schema import TextNode, NodeRelationship, RelatedNodeInfo

# Example 1
doc = Document(text="First sentence. Second sentence")
n1 = TextNode(text="First sentence.", node_id=doc.doc_id)
n2 = TextNode(text="Second sentence.", node_id=doc.doc_id)

n1.relationships[NodeRelationship.NEXT] = n2.node_id
n2.relationships[NodeRelationship.PREVIOUS] = n1.node_id

print(n1.relationships)
print(n2.relationships)
