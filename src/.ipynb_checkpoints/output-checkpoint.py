from sodapy import Socrata

def print_to_file(data,OUTPUT:str):
    with open(OUTPUT, 'a') as f:
        print(data, file=f)
        
def show_data(client,PAGE_SIZE: int, NUM_PAGES: int, OUTPUT: str, ID: str):
    ## if NUM_PAGES was not provided, set it to display all of the data
    #numPages = int(NUM_PAGES)
    pageSize = int(PAGE_SIZE)
    if numPages == -1: # -1 is the default
        dataset_size = int(client.get(ID, select ='COUNT(*)'[0]['COUNT']))
        numPages = int(dataset_size/pageSize)
    ## if output was not set, print to stdout
    if OUTPUT == -1:
        for i in range(numPages):
            data = client.get(ID, limit = pageSize, offset = i*numPages)
            print(f'\n\n\n\n\nPage number: {i+1}\n\n\n\n\n')
    # otherwise, print to file
    else: 
        for i in range(numPages):
            data = client.get(ID, limit = pageSize, offset = i*numPages)
            print_to_file(data, OUTPUT)