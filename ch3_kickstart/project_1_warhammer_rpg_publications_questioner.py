"""
This script uses LlamaIndex to load and query a Wikipedia article about Warhammer Fantasy Roleplay publications.

It includes:
- Loading the Wikipedia article with auto-suggest disabled.
- Parsing the content into nodes using SimpleFileNodeParser.
- Creating a SummaryIndex for fast retrieval.
- Enabling an interactive query loop to ask questions about different editions.

Author: Danny
Date: 2025-04-20
Version: 1.0
"""

from llama_index.core import Document, SummaryIndex, Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.readers.wikipedia import WikipediaReader
import logging

logging.basicConfig(level=logging.DEBUG)

# Initialize the OpenAI LLM with GPT-4.1-Nano
llm = OpenAI(model="gpt-4.1-nano-2025-04-14")

# Set the LLM in LlamaIndex settings
Settings.llm = llm

# Optional: Confirm the model being used
print("Model in use:", Settings.llm.model)

# Step 1, load the wikipedia article
loader = WikipediaReader()
document = loader.load_data(
    pages=[
        "List of Warhammer Fantasy Roleplay publications",
    ],
    auto_suggest=False,
)

# Step 2. parse the document into nodes
parser = SimpleFileNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(document)

# Step 3. Create the index
index = SummaryIndex(nodes)

# Step 4. Create the query engine
query_engine = index.as_query_engine()

print("Ask me questions about the different editions of warhammer fantasy rpg")

# Step 5. Logic
while True:
    question = input("Please ask me a question: ")
    if question.lower() == "exit":
        break
    response = query_engine.query(question)
    print(response)
