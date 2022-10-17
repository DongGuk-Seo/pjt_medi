import meilisearch

with open('./key.txt','r') as f:
    key = f.read()

client = meilisearch.Client('http://35.216.64.12:7700/', key)
index_num = int(input('Choose index : \n 1. product \n 2. crawling_data \n 3. articles \n  : ')) 
indexes = ['product','crawling_data','articles']

client.index(indexes[index_num-1]).reset_ranking_rules()
client.index(indexes[index_num-1]).reset_stop_words()
client.index(indexes[index_num-1]).reset_stop_words()
client.index(indexes[index_num-1]).reset_pagination_settings()
client.index(indexes[index_num-1]).reset_faceting_settings()
client.index(indexes[index_num-1]).reset_typo_tolerance()
client.index(indexes[index_num-1]).reset_searchable_attributes()
client.index(indexes[index_num-1]).reset_filterable_attributes()

print('All settings have returned!')