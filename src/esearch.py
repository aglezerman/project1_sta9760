import requests
from elasticsearch import Elasticsearch


def create_and_update_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass
    return es

def push(data_list, es):
# Send the data into es
	for i in range(len(data_list)):
		es.index(index='parking-violation-index', ignore=400, doc_type='parking-violation-type',
				id=int(data_list[i]['summons_number']), body=((data_list[i])))
		#print(data_list[i][0],'\n',type(data_list[0][0]))
