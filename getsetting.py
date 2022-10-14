import meilisearch

client = meilisearch.Client('http://35.216.64.12:7700', 'team10')
index_num = int(input('Choose index : \n 1. product_all \n 2. product_clean \n 3. crawling_data \n 4. articles \n  : ')) 
indexes = ['product_all','product_clean','crawling_data','articles']

print(client.index(indexes[index_num-1]).get_settings())