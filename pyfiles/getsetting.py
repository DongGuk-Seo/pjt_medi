import meilisearch
import os

with open('./key.txt','r') as f:
    key = f.read()

client = meilisearch.Client(os.environ['MEILI_URL'], key)
index_num = int(input('Choose index : \n 1. product \n 2. crawling_data \n 3. articles \n  : ')) 
indexes = ['product','crawling_data','articles']

print(client.index(indexes[index_num-1]).get_settings())