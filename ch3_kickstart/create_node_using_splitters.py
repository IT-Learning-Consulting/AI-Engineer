"""
Extracting nodes automatically from documents using splitters
"""

from llama_index.core import Document
from llama_index.core.node_parser import TokenTextSplitter

# Example 1
doc = Document(
    text=("This is sentence 1. This is sentence 2. This is sentence 3."),
    metadata={"author": "Joh Smith"},
)

splitter = TokenTextSplitter(chunk_size=12, chunk_overlap=0, separator=" ")

nodes = splitter.get_nodes_from_documents([doc])
for node in nodes:
    print(node.text)
    print(node.metadata)

# Example 2
doc = Document(
    text=(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sed ultricies lacus, at dapibus purus. Vivamus sollicitudin rutrum ligula, sit amet commodo purus imperdiet in. Aliquam quis nulla quis orci porttitor ultrices. In semper urna non erat faucibus pellentesque. Cras quis rutrum lectus. Nulla ac ante scelerisque felis dignissim suscipit a eu leo. Suspendisse at consectetur eros. Aenean dapibus enim purus, ut porta quam placerat a. Nullam a quam tortor. Integer in ante velit. Nam imperdiet sit amet leo non laoreet. Phasellus accumsan, elit a sodales convallis, diam ligula imperdiet quam, et hendrerit risus augue nec libero. Donec id ligula sed lectus pretium molestie in non ligula. Mauris consequat velit a lobortis fringilla. Vestibulum congue auctor mi, vitae aliquam nibh dictum quis. Maecenas efficitur iaculis cursus."
    ),
    metadata={"author": "Impsum"},
)

splitter = TokenTextSplitter(chunk_size=50, chunk_overlap=5, separator=" ")

nodes = splitter.get_nodes_from_documents([doc])
for node in nodes:
    print(node.text)
    print(node.metadata)
