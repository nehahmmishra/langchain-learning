pip install -U langchain-community pypdf

from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('/content/sample_data/Carpet_Manufacturing_Technical_Manual_Synthetic_dataset.pdf')
docs = loader.load()
print(docs)
