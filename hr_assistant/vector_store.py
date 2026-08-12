"""Step 4:  Store chunk embeddings in FAISS so that we can search later"""

import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings

#three methods build,save,load

# build vector store
def build_vector_store(chunks):
    """Embed every chunk and build
    a searchachble FAISS index in memmory."""
    embeddings_model = get_embeddings()
    return FAISS.from_documents(chunks,embeddings_model)


def save_vector_store(vector_store,path:str = config.VECTOR_STORE_PATH):
    """
    Save the FAISS vector store to disk.
    So we don't have to re-embed the chunks every time we run the app.
    """
    vector_store.save_local(path)
    
def load_vector_store(path:str = config.VECTOR_STORE_PATH):
    """"
     Load a prevviosuly saved FAISS vector store from disk.
    """    
    embeddings_model = get_embeddings()
    return FAISS.load_local(path,embeddings_model,allow_dangerous_deserialization=True)

def vector_store_exists(path:str = config.VECTOR_STORE_PATH):
    """Check if the FAISS vector store exists on disk."""
    return os.path.exists(os.path.join(path,"index.faiss")) 
 

def get_retriever(vector_store,k:int = config.TOP_K_RESULTS):
    """Turn a vector store into a retriever that
        return the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})