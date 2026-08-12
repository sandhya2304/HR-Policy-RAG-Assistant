"""Step 2. chop the document into small,searchable chunks."""

from langchain.text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

def split_into_chunks(documents) -> list:
    """Split the document into small, searchable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len
    )
    return text_splitter.split_documents(documents)