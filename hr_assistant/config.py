#"ALL rights reserved. No part of this code may be reproduced,
 #distributed, or transmitted in any form or by any means,
 #including photocopying, recording, or other electronic or 
 #mechanical methods, without the prior written permission of the 
 #copyright owner, except in the case of brief quotations 
 #embodied in critical reviews and certain other noncommercial
 #uses permitted by copyright law. For permission requests,
 #write to the publisher at the address below."
 
"""All settings for the app live here,in one place"""

import os
from dotenv import load_dotenv

load_dotenv()


## Env var / secrets
Groq_API_KEY = os.getenv("GROQ_API_KEY")
Jina_API_KEY = os.getenv("JINA_API_KEY")

## Define path - Data/vector store

DATA_FILE_PATH = os.path.join("data","hr_policy.txt")
#vector stores 


#in memory
#persistent memory - vectors 100gb
#cloud memory

VECTOR_STORE_PATH = os.path.join("data","faiss_index")

#models
#llm and embedding models

LLM_MODEL_NAME = "openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME = "jina-embedding-v2-base-en"

#chunk /text splitting
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

#Retrieval results
TOP_K_RESULTS = 3

##system instructiosn

SYSTEM_PROMPT = """You are a helpful HR assistant that answers 
  questions based on the context provided.
If the context does not contain the answer, 
          respond with "I don't know" """
          
          
def check_api_keys() -> None:
    if not Groq_API_KEY:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    if not Jina_API_KEY:
        raise ValueError("JINA_API_KEY is not set in the environment variables.")