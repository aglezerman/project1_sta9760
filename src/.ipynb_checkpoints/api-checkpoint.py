from sodapy import Socrata

API_URL = 'data.cityofnewyork.us'
DATABASE_ID = 'nc67-uf89'

def get_data(APP_TOKEN):
    # call api and get data
    try:
        client = Socrata(API_URL,APP_TOKEN)
        return client
    except Exception as e:
        print(f'Error connecting to API: {e}')
        
