"""
Use user specific model
"""

from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14")
