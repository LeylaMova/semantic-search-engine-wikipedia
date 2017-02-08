#!/Users/Leyla/anaconda/bin/python
import pandas as pd
import numpy as np
import re
from sklearn.externals import joblib
from sklearn.neighbors import NearestNeighbors


def search_query(terms, top=True):

    df = pd.read_pickle('data/df.pkl')
    vecs = joblib.load('data/vecs.pkl')
    lsa = joblib.load('data/lsa.pkl')

    terms = [terms]
    search = lsa.transform(terms)[0]
    highlight_terms = terms[0].split()
        
    nbrs = NearestNeighbors(n_neighbors=5).fit(vecs)
    indecies = nbrs.kneighbors(search.reshape(1, -1))[1][0].tolist()
    
    if top:
        for i in indecies:
            print 'Title:', df.iloc[i]['title']
            print 'Summary:', df.iloc[i]['page'][:300]
            print   
    
    else:
        title = df.iloc[indecies[0]]['title']
        text = df.iloc[indecies[0]]['page']
   
    
        for word in highlight_terms:
            regex = re.compile(r'\b('+'|'.join(highlight_terms)+r')s?', 
                               flags=re.IGNORECASE | re.VERBOSE) 

            subst = '\033[43;30m' + r'\g<0>' + '\033[0m'
            result = re.sub(regex, subst, text)
        
        print 'Title:', title
        print 'Text:', result 

           
    
    
    
    
    
    
    
    
    
    
    






