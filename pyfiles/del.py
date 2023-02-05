import meilisearch
import os

with open('./key.txt','r') as f:
    key = f.read()

client = meilisearch.Client(os.environ['MEILI_URL'], key)

client.index(input()).delete()