from sodapy import Socrata

DATABASE_ID = 'nc67-uf89'

# when called, this function will print the data to a file
def print_to_file(data,output:str):
    with open(output, 'a') as f:
        print(data, file=f)
        
def show_data(client,page_size: int, num_pages: int, output: str):
    ## if NUM_PAGES was not provided, set it to display all of the data
    try:
        numPages = int(num_pages)
        pageSize = int(page_size)
    except:
        print("Input error. enter num pages and page size as integers (whole number)")
    if numPages == -1: # -1 is the default. if no input was given, set num pages to ALL pages 
        dataset_size = int(client.get(DATABASE_ID, select ='COUNT(*)')[0]['COUNT'])
        numPages = int(dataset_size/pageSize)
    ## if output was not set, print to stdout
    if output == -1:
        for i in range(numPages):
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
            print(f'\n\n\n\n\nPage number:{i+1}\n\n\n\n{data}\n\n\n')
    # otherwise, print to file
    else: 
        for i in range(numPages):
            data = client.get(DATABASE_ID, limit = pageSize, offset = i*numPages)
            print_to_file(data, output)