import meilisearch
import os

with open('./key.txt','r') as f:
    key = f.read()

client = meilisearch.Client(os.environ['MEILI_URL'], key)

index_name = input("Index name : ")
PK = input("\n PK : ")

client.create_index(index_name, {'primaryKey' : PK})