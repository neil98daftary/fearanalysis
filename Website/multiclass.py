# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:26:42 2017

@author: jaideeprao
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import math
Main_Path = "/home/neil/Desktop/fearanalysis/Website"
os.chdir(Main_Path)

import re
# import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
# nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.svm.libsvm import  predict_proba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

anothercorpus = []
stop_words = set(stopwords.words('english'))
stop_words.remove('not')
retrieved_model = joblib.load("model.pkl")
retrieved_vectorizer = CountVectorizer(vocabulary = joblib.load("vectorizer.pkl"))

def preprocessing(testvar):
    testing = re.sub('[^a-zA-Z]', ' ', testvar)
    testing = testing.lower()
    testing = word_tokenize(testing)
    ps = PorterStemmer()
    testing = [ps.stem(word) for word in testing if not word in stop_words]
    testing = ' '.join(testing)
    print testing
    anothercorpus.append(testing)


def predictionFunction(R):
    # probs1 = retrieved_model.predict_proba(R)
    probs11 = retrieved_model.predict(R)[-1]
    print(probs11)
    return probs11

def process(answer):
    preprocessing(answer)
    R = retrieved_vectorizer.transform(anothercorpus).todense()
    return predictionFunction(R)
