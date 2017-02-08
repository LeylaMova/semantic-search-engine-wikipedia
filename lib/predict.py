#!/Users/Leyla/anaconda/bin/python
import string
from sklearn.externals import joblib

def text_cleaner(doc):
    doc = doc.lower().translate(None, string.punctuation).replace('\n',' ')
    return [doc]

def predict(document):
    model = joblib.load('data/model.pkl')
    
    doc = text_cleaner(document)
    doc_vec = model[0].transform(doc)
    cat = model[1].predict(doc_vec)[0]
    conf = model[1].predict_proba(doc_vec).sum()

    print 'Predict Category:', cat
    print 'Confidence:', conf