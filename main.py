import requests
import sys
import argparse
from src.api import get_data
from src.output import present_data

variables = argparse.ArgumentParser()

variables.add_argument('--PAGE_SIZE', type = int, required = True)
variables.add_argument('--NUM_PAGES', type = int, default = -1)
variables.add_argument('--OUTPUT', type = str, default = -1)

args = variables.parse_args()

app_token = os.environ['APP_KEY']

PAGE_SIZE = args.page_size
NUM_PAGES = args.num_pages
OUTPUT = args.output

client = get_data(app_token)
present_data(client, PAGE_SIZE, NUM_PAGES, OUTPUT)