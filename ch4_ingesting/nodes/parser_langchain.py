from pathlib import Path
from llama_index.core import Settings
from llama_index.core.node_parser import LangchainNodeParser
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import FlatReader
from langchain.text_splitter import CharacterTextSplitter


# Set the global LLM to GPT-4.1-Nano
Settings.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.8)

print("Model in use:", Settings.llm.model)

reader = FlatReader()

document = reader.load_data(Path("../files/documents/the_empire.md"))

parser = LangchainNodeParser(CharacterTextSplitter())

nodes = parser.get_nodes_from_documents(document)

for index, node in enumerate(nodes):
    print(node.text)
    print(node.metadata)
    print(f"(INDEX: {index})")
    print(f"LENGTH: {len(node.text)}\n")
