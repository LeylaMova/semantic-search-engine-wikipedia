import requests
from collections import OrderedDict
from bs4 import BeautifulSoup
from helpers import param_query, cat_param_id, cat_param_pages, page_params, text_cleaner, get_summary


#actual functions
def query_category(category):
    """
    
    Takes category name and returns a dictionary with category id and a list of pages (page id and title) associated with that category.
    
    """
    base_url = "https://en.wikipedia.org/w/api.php"
    
    param_one = cat_param_id(category)
    query_one = param_query(param_one)
    response_one = requests.get(base_url+query_one)
    categoryid = response_one.json()['query']['pages'].keys()[0]
    
    param_two = cat_param_pages(category)
    query_two = param_query(param_two)
    response_two = requests.get(base_url+query_two)
    pages = response_two.json()['query']['categorymembers']
    
    return {'categoryid':categoryid,'pages':[{'pageid':page['pageid'],'title':(
                        page['title'])} for page in pages]}


def query_page(pageid,title):
    """
    
    Takes page id and title to return a dictionary with page id, summary, plain text and original html that was extracted from wikipedia.
    
    """
    base_url = "https://en.wikipedia.org/w/api.php"    
    
    query = param_query(page_params(pageid))
    response = requests.get(base_url+query)
    html = response.json()['query']['pages'][pageid]['extract']

    cleantext = BeautifulSoup(html,'lxml').text
    cleantext = text_cleaner(cleantext)
    summary = get_summary(cleantext)
    
    return OrderedDict([('pageid',int(pageid)),('title',title),('summary',summary),('text',cleantext),('html',html)])


