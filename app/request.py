from app import app
import urllib.request,json
from .models import quotes

Quotes = quotes.Quotes

quotes_api = app.config['QUOTES_API']
base_url = app.config['QUOTES_API_BASE_URL']


def get_quotes(random):
    '''
    function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(random,quotes_api)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['results']:
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quotes_results_list)


    return quotes_results



def process_results(quotes_list):
    '''
    Function that processes the movie result and transform them to a list of objects

    Args:
       quotes_list: A list of dictionaries that contain quotes details

    Return :
        quotes_results: A list of quotes objects

    '''
    quotes_results = []
    for quotes_item in quotes_list:
      author = quotes_item.get('author')
      id = quotes_item.get('id')
      quote = quotes_item.get('quotes')
      permalink = quotes_item.get('permalink')
    

      if quotes:
          quotes_object = Quotes(author, id, quote, permalink )

          quotes_results.append(quotes_object)

    return quotes_results
        