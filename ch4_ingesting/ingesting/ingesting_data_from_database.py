"""
This script demonstrates how to use the LlamaIndex DatabaseReader to load data from an SQLite database,
alongside configuring a global LLM model for further processing.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Connecting to an SQLite database using a URI.
- Executing an SQL query to retrieve data from the 'products' table.
- Printing the text content of each retrieved document.

Useful for integrating structured database content into a language model workflow for analysis, indexing, or summarization.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.readers.database import DatabaseReader

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)


reader = DatabaseReader(uri="sqlite:///files/example.db")

query = "SELECT * FROM products"
documents = reader.load_data(query=query)

for doc in documents:
    print(doc.text)
