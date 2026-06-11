pip install -U langchain-text-splitters

#Length based text splitting
from langchain_text_splitters import CharacterTextSplitter
text=""" Artificial intelligence firm Anthropic has launched a $200 million initiative to examine how AI will reshape employment and economic growth, while urging governments to prepare for potentially severe labour market disruptions as the technology becomes more powerful.
The announcement was accompanied by a new policy framework and a detailed essay from Anthropic chief executive Dario Amodei, who argued that AI could transform the workforce more rapidly and more extensively than previous technological revolutions.

Amodei said policymakers and businesses should begin preparing now for scenarios in which automation significantly reduces demand for human labour.

The key challenge in such a world won't be incentivizing growth, but finding a way for everyone to s...
"""
splitter= CharacterTextSplitter(chunk_size=100,chunk_overlap=3,separator='') 
result=splitter.split_text(text)
print(result)
