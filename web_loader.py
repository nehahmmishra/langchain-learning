from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader ('https://obeetee.com/')
docs = loader.load()
print (docs)
print(docs[0].page_content[:1000])
