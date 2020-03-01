import requests
import sys
import argparse
import os
from src.api import get_data
from src.output import show_data

variables = argparse.ArgumentParser()

variables.add_argument('--page_size', type = int, required = True)
variables.add_argument('--num_pages', type = int, default = -1)
variables.add_argument('--output', type = str, default = -1)

args = variables.parse_args()

app_token = os.environ['APP_KEY']

page_size = args.page_size
num_pages = args.num_pages
output = args.output

client = get_data(app_token)
show_data(client, page_size, num_pages, output)