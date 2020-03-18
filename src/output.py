from sodapy import Socrata
from datetime import datetime

DATABASE_ID = 'nc67-uf89'

# when called, this function will print the data to a file
def print_to_file(data,output:str):
    print(f'Printing to file {output}')
    with open(output, 'a') as f:
        print(data, file=f)

### make a function to get the data
#def get_data:
'''
def show_data(client,page_size: int, num_pages: int, output: str):
    ## if NUM_PAGES was not provided, set it to display all of the data
    try:
        numPages = int(num_pages)
        pageSize = int(page_size)
    except Exception as e:
        print(f"Input error. enter num pages and page size as integers (whole number) : {e}")
    print('fetching......')
    if numPages == -1: # -1 is the default. if no input was given, set num pages to ALL pages 
        dataset_size = int(client.get(DATABASE_ID, select ='COUNT(*)')[0]['COUNT'])
        numPages = int(dataset_size/pageSize)
    ## if output was not set, print to stdout
    if output == -1:
        for i in range(numPages):
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
            print(f'\nPage number:{i+1}\n\n\n\n{data}\n\n\nType: {type(data)}')
    # otherwise, print to file
    elif output == 'es':
        data_list = []
        # preps data to load to elasticsearch
        for i in range(numPages):
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
            # convert issue_date field into a datetime format
            for j in range(pageSize):
                #print(data[j]['issue_date'])
                data[j]['issue_date'] = datetime.strptime(data[j]['issue_date'],'%m/%d/%Y')
                for k in data[j]:
                    try:
                        data[j][k] = int(data[j][k])
                    except:
                        pass
                data_list.append(data[j])
        return data_list
    else: 
        for i in range(numPages):
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
            print_to_file(data, output)
'''
#ver 1.1
def show_data(client,page_size: int, num_pages: int, output: str):
    ## if NUM_PAGES was not provided, set it to display all of the data
    try:
        numPages = int(num_pages)
        pageSize = int(page_size)
    except Exception as e:
        print(f"Input error. enter num pages and page size as integers (whole number) : {e}")
    print('fetching......')

    if numPages == -1: # -1 is the default. if no input was given, set num pages to ALL pages 
        dataset_size = int(client.get(DATABASE_ID, select ='COUNT(*)')[0]['COUNT'])
        numPages = int(dataset_size/pageSize)
    data_list = []

    for i in range(numPages):
        try:
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
        except Exception as e:
            print(f"Error fetching data: {e}")
        
        # default output, print to stdout
        if output == -1:
            print(f'\nPage number:{i+1}\n\n{data}\n\n\n')
        # print to elasticsearch
        elif output == 'es':
            for j in range(pageSize):
                data[j]['issue_date'] = datetime.strptime(data[j]['issue_date'],'%m/%d/%Y')
                data_list.append(data[j])
        # print to file
        else:
            try:
                print_to_file(data, output)
            except Exception as e:
                print(f"Error printing to file : {e}")

    if output == 'es':
        return data_list
