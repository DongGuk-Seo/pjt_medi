import meilisearch

client = meilisearch.Client('http://35.216.64.12:7700/', 'team10')

index_name = input("Index name : ")
PK = input("\n PK : ")

client.create_index(index_name, {'primaryKey' : PK})