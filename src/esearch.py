import requests
from elasticsearch import Elasticsearch


def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    if es.indices.exists(index=index_name):
        return es
    else:
        try:
            es.indices.create(index=index_name)
        except Exception as e:
            print(f'Error creating index {e}')
            pass
    return es


def push(data_list,es):
# Send the data into es
    try:
        print("loading to elasticsearch")
        for i in range(len(data_list)):
            es.index(index='parking-violation-index', ignore=400, doc_type='parking-violation',
                id=int(data_list[i]['summons_number']), body=((data_list[i])))
    except Exception as e:
        print(f'Error loadint to es: {e}')
