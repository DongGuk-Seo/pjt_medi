import meilisearch

with open('key.txt','r') as f:
    key = f.read()

client = meilisearch.Client('http://35.216.64.12:7700/', key)

index_name = input("Index name : ")
PK = input("\n PK : ")

client.create_index(index_name, {'primaryKey' : PK})