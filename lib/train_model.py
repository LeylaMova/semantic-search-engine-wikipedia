#!/Users/Leyla/anaconda/bin/python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from lib.project_5 import general_estimator, general_transformer


def train_model(model):
    page_cat = pd.read_pickle('data/page_cat.pkl')
    X = page_cat['page']
    y = page_cat['category_name']

    lsa = Pipeline([('vectorizer', TfidfVectorizer(stop_words='english')),
                ('normalize', Normalizer(copy=False)),
                ('svd', TruncatedSVD(n_components=17,n_iter=10,random_state=42))])

    data_dict = general_transformer(lsa, X, y)
    data_dict = general_estimator(model, data_dict, random_state=42)
    joblib.dump(lsa, 'data/lsa.pkl') 

    return data_dict
    