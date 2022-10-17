import meilisearch

with open('./key.txt','r') as f:
    key = f.read()

client = meilisearch.Client('http://35.216.64.12:7700', key)
index_num = int(input('Choose index : \n 1. product \n 2. crawling_data \n 3. articles \n  : ')) 
indexes = ['product','crawling_data','articles']

print(client.index(indexes[index_num-1]).get_settings())