from sodapy import Socrata
from datetime import datetime
#
from src.esearch import create_and_update_index, push

DATABASE_ID = 'nc67-uf89'

# when called, this function will print the data to a file
def print_to_file(client,page_size: int, num_pages: int, output: str):
    print(f'Printing to file {output}')
    with open(output, 'a') as f:
        for i in range(num_pages):
            data = get_data(client,page_size, num_pages, i)
            print(data, file=f)

# this function is used to get the data from the database
def get_data(client,page_size: int, num_pages: int, i: int):
    try:
        data = client.get(DATABASE_ID, limit = page_size, offset = i*num_pages)
    except Exception as e:
        print(f'error fetching data! code : {e}')
        raise

    return data

# this function preps the page_size and num_pages to work , or set to default
def prep_vars(client,page_size: int, num_pages: int):
    ## if NUM_PAGES was not provided, set it to display all of the data
    try:
        num_pages = int(num_pages)
        page_size = int(page_size)
        if num_pages == -1: # -1 is the default. if no input was given, set num pages to ALL pages 
            dataset_size = int(client.get(DATABASE_ID, select ='COUNT(*)')[0]['COUNT'])
            num_pages = int(dataset_size/pageSize)
    except Exception as e:
        print(f"Error. make sure num pages and page size as integers (whole number) : {e}")
        raise

    return num_pages,page_size

# loads the data to esearch
def load_to_es(client,page_size: int, num_pages: int):
    data_list = []
    for i in range(num_pages):
        data = get_data(client,page_size, num_pages, i)
        for j in range(page_size):
            data[j]['issue_date'] = datetime.strptime(data[j]['issue_date'],'%m/%d/%Y')
            for k in data[j]:
                try: # convery non string/empty cells to int. this way i load the number parts of the data as numbers 
                    data[j][k] = int(data[j][k])
                except:
                    pass
            data_list.append(data[j])
    es = create_and_update_index('parking-violation-index','parking-violation')
    push(data_list,es)

# this function sends the data to stdout
def print_to_stdout(client,page_size: int, num_pages: int):
    page_size,num_pages = prep_vars(client,page_size,num_pages)
    for i in range(num_pages):
        data = get_data(client,page_size, num_pages, i)
        print(f'\nPage number:{i+1}\n\n{data}\n\n\n')

# data handler, sends to the correct function
def data_handler(client,page_size: int, num_pages: int, output: str):

    page_size,num_pages = prep_vars(client,page_size,num_pages)
    if output == -1:
        print_to_stdout(client,page_size, num_pages)      
    elif output == 'es':
        load_to_es(client,page_size, num_pages)
    else:
        print_to_file(client,page_size, num_pages, output)
