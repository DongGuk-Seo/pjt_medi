import meilisearch

with open('key.txt','r') as f:
    key = f.read()

client = meilisearch.Client('http://35.216.64.12:7700/', key)

client.index(input()).delete()