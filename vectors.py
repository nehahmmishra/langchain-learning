pip install langchain chromadb openai tiktoken pypdf langchain-openai langchain-community

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings # free embedding model as openAiEmbeddings needs API

docs = [
    Document(
        page_content="Virat Kohli is one of India's greatest batsmen. He has scored more than 80 international centuries and was the captain of India across formats.",
        metadata={"team": "India"}
    ),

    Document(
        page_content="Rohit Sharma is known for elegant batting and holds the record for the highest individual ODI score of 264 runs. He captains India in major tournaments.",
        metadata={"team": "India"}
    ),

    Document(
        page_content="Ben Stokes is an English all-rounder famous for match-winning performances. He played a crucial role in England winning the 2019 Cricket World Cup.",
        metadata={"team": "England"}
    ),

    Document(
        page_content="Babar Azam is one of Pakistan's top batsmen. He is known for consistency across formats and has been ranked among the best ODI batters.",
        metadata={"team": "Pakistan"}
    ),

    Document(
        page_content="Pat Cummins is an Australian fast bowler and captain. He helped Australia win both the World Test Championship and ODI World Cup in 2023.",
        metadata={"team": "Australia"}
    )
]

# vector_store = Chroma(
#     embedding_function=OpenAIEmbeddings(),
#     persist_directory='Chroma_db',
#     collection_name='cricketers'
# )

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_store = Chroma(
    embedding_function=embedding,
    persist_directory="chroma_db",
    collection_name="cricketers"
)

#add documents
vector_store.add_documents(docs)

#view documents
vector_store.get(include=['embeddings','documents','metadatas'])

#search documents
vector_store.similarity_search(
    query='who among these are best batsman?',k=1
)

#search with smilarity score
vector_store.similarity_search_with_score(
    query='who among these bowler', k=2
)
