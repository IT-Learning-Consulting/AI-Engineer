""" """

from llama_index.core import Document, SummaryIndex
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.readers.wikipedia import WikipediaReader

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
