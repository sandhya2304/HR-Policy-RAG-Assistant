"""Step 3: Turn text into numbers(vectors)"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings(texts: list) :
    """Return a Jina Embeddings model.
    Read JINA_API_KEY from the environment.

    """
    return JinaEmbeddings(model_name=config.EMBEDDINGS_MODEL_NAME)
