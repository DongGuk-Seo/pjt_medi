import meilisearch
import json
import re

client = meilisearch.Client('http://localhost:7700', 'masterKey')
a = 'products_new'
# An index is where the documents are stored.
index = client.index(a)

client.create_index(f'{a}', {'primaryKey':'_id'})

json_file = open(f'data/product/{a}.json',encoding='utf-8')
documents = json.load(json_file)

# Remove dict type -> Json in Json 
# "$date"
date_list = ['date_created','date_updated','date_sale_from','date_sale_to',]
for x in date_list:
    for i in range(len(documents)):
        if x in documents[i].keys():
            if documents[i][x] != None and "$date" in documents[i][x].keys():
                documents[i][x] = documents[i][x]['$date']
            else:
                pass

# "$oid"
id_list = ['_id','category_id']
for x in id_list:
    for i in range(len(documents)):
        if x in documents[i].keys():
            if documents[i][x] != None and "$oid" in documents[i][x].keys():
                documents[i][x] = documents[i][x]['$oid']

# image
for i in range(100):
    src = re.findall('',documents[i]['description'])
    if src != []:
        print(src[0])
    # if src != []:
    #     documents[i]['image'] = src[0][10:]
    # else:
    #     documents[i]['image'] = ''

# description cleaning
for i in range(len(documents)):
    documents[i]['description'] = re.sub('&[a-z]*;|nbsp|<[^>]+>|lsquo|rsquo|rdquo|ldquo|;',' ',documents[i]['description'])



# Add documents
index.add_documents(documents) # => { "uid": 0 }

# img : img src[^>]+.png|img src[^>]+.jpg
# regex : &[a-z]*;|nbsp|<[^>]+>|lsquo|rsquo|rdquo|ldquo|;
print("done!")