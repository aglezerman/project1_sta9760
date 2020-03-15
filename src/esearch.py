import requests
import json
import os
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
		es.index(index='myindex', ignore=400, doc_type='parking-violation-type',
				id=i, body=((data_list[i][0])))
		#print(data_list[i][0],'\n',type(data_list[0][0]))



'''
es.indices.put_mapping(
    index='violation-index',
    doc_type='parking-violation-type',
    body={
        'parking-violation-type': {
            'properties': {
				'plate': {'type': 'string'}, 
				'state': {'type': 'string'}, 
				'license_type': {'type': 'string'}, 
				'summons_number': {'type': 'integer'}, 
				'issue_date': {'type': 'date'}, 
				'violation_time': {'type': 'string'}, 
				'violation': {'type': 'string'}, 
				'fine_amount': {'type': 'integer'}, 
				'penalty_amount': {'type': 'integer'}, 
				'interest_amount': {'type': 'integer'}, 
				'reduction_amount': {'type': 'integer'}, 
				'payment_amount': {'type': 'integer'}, 
				'amount_due': {'type': 'integer'}, 
				'precinct': {'type': 'string'}, 
				'county': {'type': 'string'}, 
				'issuing_agency': {'type': 'string'}, 
				'summons_image': {'type': 'string'}, 
				'description': {'type': 'string'}
							}
			                		}
			}
						)
'''
