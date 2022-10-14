import meilisearch

client = meilisearch.Client('http://35.216.64.12:7700', 'team10')

index_num = int(input('Choose index : \n 1. product_all \n 2. crawling_data \n  : '))
indexes = ['product_all','crawling_data']

a = client.index(indexes[index_num-1]).search(input('Search : '),{'limit':20})
print(a)