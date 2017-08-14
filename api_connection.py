'''
First Geru's Challenge:
to create a lib to connect to the API at the following address:

https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes

'''

import requests
import json

def main_quotes_path(path = ''):
    '''main_quotes_path returns the whole url as string.
       If no path is passed to it, only the main url address returns,
       otherwise it will either load the main /quotes or one specific quote, for example /quotes/3'''
    return 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge' + path

def get_quotes():
    '''get_quotes returns the main /quotes.'''
    return requests.get(main_quotes_path('/quotes/')).json()

def get_quote(quote_id):
    '''get_quote receives an integer related to the quote desired.
       quote index start from 0 (zero)!'''
    return requests.get(main_quotes_path('/quotes/{:d}/'.format(int(quote_id)))).json()
