import math
from urllib import quote
from unidecode import unidecode


#helper functions
def param_query(params):
    """
    
    Takes wikipedia parameters, converts, and returns it into appropriate query     format. 
    
    """
    param_list = [key+'='+str(value) for key,value in params.items()] 
    return '?'+'&'.join(param_list)

def cat_param_id(category):
    """
    
    Takes category name, formats, and adds it to wikipedia endpoint dictionary to extract category info.    
    
    """
    params = { 'action':'query',
               'format':'json',              
               'prop':'extracts',
               'exlimit':'maxl',
               'titles':'Category:'+quote(category)}
    return params

def cat_param_pages(category):
    """
    
    Takes category name, formats, and adds it to wikipedia endpoint dictionary to get a list of pages associated with that category.  
    
    """
    params = { 'action':'query',
               'format':'json',              
               'list':'categorymembers',
               'cmlimit':'max',
               'cmtype':'page',
               'cmtitle':'Category:'+quote(category)}
    return params

def page_params(pageid):
    """    
    
    Takes pageid and adds it to wikipedia endpoint dictionary to extract the content of the page.      
    
    """
    params = { 'action':'query',
               'format':'json',              
               'prop':'extracts',
               'exlimit':'maxl',
               'pageids':quote(pageid)}
    return params

def text_cleaner(text):
    """    
    
    Takes wikipedia page content and cleans their formatting to return plain text.  
    
    """
    text = " ".join(text.split()).replace("\'","").replace("/"," ").replace(r"[...]","")
    return text

def get_summary(text):
    """
    
    Takes plain text and returns the first 2 sentences as summary.  
    
    """
    summary = '.'.join(text.split('.')[:2])
    return summary 

def dotproduct(v1, v2):
    """
    
    Takes 2 vectors and multiplies them.  
    
    """
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    """
    
    Takes a vectors and gets the square root. 
    
    """
    return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    """
    
    Takes 2 vectors and gets the cosine similarity and returns angle.
    
    """
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
