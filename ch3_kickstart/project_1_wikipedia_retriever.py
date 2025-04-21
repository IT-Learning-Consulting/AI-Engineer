"""
This script loads a Wikipedia article using LlamaIndex, parses it into nodes, and builds a SummaryIndex for interactive querying.

It includes:
- Loading Lionel Messi's Wikipedia page.
- Parsing the document into TextNodes using SimpleFileNodeParser.
- Indexing the nodes and enabling a loop for user-driven queries.

Useful for testing LlamaIndex's ability to handle real-world documents and support interactive Q&A.

Author: Danny
Date: 2025-04-20
Version: 1.0
"""

from llama_index.core import Document, SummaryIndex
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.readers.wikipedia import WikipediaReader

# Load Wikipedia article about Lionel Messi
loader = WikipediaReader()
documents = loader.load_data(pages=["Messi Lionel"])

# Parse the document into nodes
parser = SimpleFileNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)

# Create a summary index from the parsed nodes
index = SummaryIndex(nodes)

# Create a query engine for interactive use
query_engine = index.as_query_engine()

print("Ask me anything about Lionel Messi!")

# Start an interactive query loop
while True:
    question = input("Your question: ")
    if question.lower() == "exit":
        break  # Exit the loop when the user types "exit"
    response = query_engine.query(question)  # Perform the query
    print(response)  # Print the response
