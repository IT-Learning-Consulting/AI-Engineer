"""
This script demonstrates how to use the LlamaIndex NotionPageReader to extract content from a Notion page,
while configuring a global LLM model for downstream processing.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Authenticating access to Notion using an integration token.
- Loading data from a specific Notion page using its page ID.
- Printing the text content extracted from the Notion page.

Useful for processing Notion-based content such as notes, documents, and project pages for use in
LLM-powered applications like summarization, indexing, and knowledge base construction.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.readers.notion import NotionPageReader

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

# Load .env file
load_dotenv()

notion_token = os.getenv("NOTION_TOKEN")

# Initialize NotionPageReader
reader = NotionPageReader(
    integration_token=notion_token,
)

# Load Data from Notion
documents = reader.load_data(page_ids=["1d85e69f6c1a803eb0a5c04ae4c664c0"])

for doc in documents:
    print(doc.text)
