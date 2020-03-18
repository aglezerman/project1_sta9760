## import dependencies from known python packages
import requests
import sys
import argparse
import os
## import functions from src subfolder
from src.api import get_data
from src.output import show_data
#
from src.esearch import create_and_update_index, push

# create variables to be passed in command line
variables = argparse.ArgumentParser()
# page size is required
variables.add_argument('--page_size', type = int, required = True)
# num pages is not required, if not provided will ask for all of the data
variables.add_argument('--num_pages', type = int, default = -1)
# output is not required. if provided, stdout will print to a file
variables.add_argument('--output', type = str, default = -1)

args = variables.parse_args()

# app key environment variable 
app_token = os.environ['APP_KEY']

page_size = args.page_size
num_pages = args.num_pages
output = args.output

client = get_data(app_token)
if output == 'es':
	data_list = show_data(client, page_size, num_pages, output)
	es = create_and_update_index('parking-violation-index','parking-violation')
	push(data_list,es)
else:
	show_data(client, page_size, num_pages, output)