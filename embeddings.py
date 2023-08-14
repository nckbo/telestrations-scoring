
import openai
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

import os
import json
import time

openai.api_key = "YOUR_API_KEY"

EMBEDDINGS_PATH = 'embeddings_backup.json'

def add_embeddings(texts, model="text-embedding-ada-002", embeddings_path=EMBEDDINGS_PATH):
    # Load the existing backup or start with an empty dictionary.
    if os.path.exists(embeddings_path):
        with open(embeddings_path, 'r') as f:
            embeddings_backup = json.load(f)
    else:
        embeddings_backup = {}

    for text in texts:
        cleaned_text = text.replace("\n", " ")

        # Only compute embeddings for texts that aren't in the backup already.
        if cleaned_text not in embeddings_backup:
            response = openai.Embedding.create(input=cleaned_text, model=model)
            print(f'Getting {cleaned_text} from OpenAI')
            embedding = response['data'][0]['embedding']
            embeddings_backup[cleaned_text] = embedding
            time.sleep(0.2)  # To ensure we don't hit rate limits, adjust as needed.

    # Save the updated backup to the JSON file.
    with open(embeddings_path, 'w') as f:
        json.dump(embeddings_backup, f)

def load_embeddings(embeddings_path=EMBEDDINGS_PATH):
    """
    Load and return the saved embeddings dictionary.

    :param embeddings_path: Path to the JSON file storing the embeddings backup.
    :return: Dictionary of text-to-embedding mappings.
    """

    if os.path.exists(embeddings_path):
        with open(embeddings_path, 'r') as f:
            return json.load(f)
    else:
        return {}



def get_cosine_similarity(embedding1, embedding2):
    embedding1=np.array(embedding1).reshape(1, -1)
    embedding2=np.array(embedding2).reshape(1, -1)
    similarity=cosine_similarity(embedding1, embedding2)
    return similarity[0][0]

#%%
