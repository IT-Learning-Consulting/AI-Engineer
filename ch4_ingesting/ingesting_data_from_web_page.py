"""
This script demonstrates how to use the LlamaIndex SimpleWebPageReader to load text content from web URLs,
as well as how to configure a global LLM model for later processing.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Defining a list of URLs to scrape.
- Using SimpleWebPageReader to extract and process web content.
    - Example 1: Loading content from the LlamaIndex documentation site.
    - Example 2: Loading content from the Foundry VTT API documentation using HTML-to-text conversion.
    - Example 3: Adding custom metadata to each document, including tags and authors for contextual tracking.

Useful for ingesting and processing online documentation for downstream tasks such as indexing, querying, or summarizing.

Author: Danny
Date: 2025-04-21
Version: 1.2
"""

from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

# Example 1
urls = ["https://docs.llamaindex.ai"]

documents = SimpleWebPageReader().load_data(urls)

for doc in documents:
    print(doc.text)


# Example 2
urls = ["https://foundryvtt.com/api/"]

documents = SimpleWebPageReader(html_to_text=True).load_data(urls)

for doc in documents:
    print(doc.text)


# Example 3
def page_data(url):
    """
    Generate metadata for a given URL.

    Args:
        url (str): The URL of the web page being processed.

    Returns:
        dict: A dictionary containing metadata including the URL, a tag, and an author.
    """

    return {"url": url, "tag": "warhammer", "author": "Cubicle 7"}


urls = ["https://cubicle7games.com/wfrp-the-imperial-zoo"]

documents = SimpleWebPageReader(metadata_fn=page_data).load_data(urls)

for doc in documents:
    print(doc.metadata)
