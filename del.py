import meilisearch

client = meilisearch.Client('http://35.216.64.12:7700/', 'team10')

client.index(input()).delete()