"""
This script demonstrates how to use the LlamaIndex YoutubeTranscriptReader to extract transcripts from YouTube videos,
alongside configuring a global LLM model for later processing.

It includes:
- Setting a global language model (GPT-4.1-Nano) using LlamaIndex Settings.
- Loading a transcript from a specific YouTube video using its URL.
- Printing the text content of the retrieved transcript document.

Useful for ingesting video content into text-based pipelines for summarization, indexing, or question-answering workflows.

Author: Danny
Date: 2025-04-21
Version: 1.0
"""

from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.readers.youtube_transcript import YoutubeTranscriptReader


# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

loader = YoutubeTranscriptReader()

documents = loader.load_data(
    ytlinks=[
        "https://www.youtube.com/watch?v=nhNlrB8yiSU&list=PLG49S3nxzAnnOmvg5UGVenB_qQgsh01uC&index=46"
    ]
)

for doc in documents:
    print(doc.text)
