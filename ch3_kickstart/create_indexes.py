"""
This script demonstrates how to build a SummaryIndex using LlamaIndex and query it with natural language questions.

It includes:
- Creation of multiple TextNode instances with facts about Lionel Messi.
- Indexing those nodes using SummaryIndex.
- Performing example queries to retrieve specific information.

Useful for learning how to create simple retrieval systems with a small set of structured nodes.

Author: Danny
Date: 2025-04-20
Version: 1.0
"""

from llama_index.core import Document, SummaryIndex, Settings
from llama_index.core.schema import TextNode
import llama_setting


print("Model in use:", Settings.llm.model)

nodes = [
    TextNode(text="Lionel Messi is a football player from Argentina"),
    TextNode(text="He has won the Ballon d'Or trophy 7 times"),
    TextNode(text="Lionel Messi's hometown is Rosario."),
    TextNode(text="He was born on June 24, 1987"),
]

index = SummaryIndex(nodes)
query_engine = index.as_query_engine()

response = query_engine.query("What is Messi's hometown?")
response2 = query_engine.query("How many times has Messi won the Ballon d'Or?")
response3 = query_engine.query("For what team does Messi has played?")
print(response)
print(response2)
