#Document Structure Based Text Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
text = """def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True"""

splitter = RecursiveCharacterTextSplitter.from_language(language = Language.PYTHON,chunk_size=120,chunk_overlap=0)
chunks = splitter.split_text(text)
print (chunks)
