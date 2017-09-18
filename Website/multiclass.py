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
Main_Path = "/home/jaideeprao/Desktop"
os.chdir(Main_Path)

# dataset = pd.read_csv('rej.csv', delimiter='\t', quoting=3, sep=';')
#
# import re
# import nltk
# import sklearn
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
#
# number_of_classes = 5
#
# corpus = []
# corpus_water = []
# corpus_heights = []
# corpus_rejection = []
# corpus_lonliness = []
#
# for i in range(0, 15):
#   review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
#   review = review.lower()
#   review = review.split()
#   ps = PorterStemmer()
#   review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
#   review = ' '.join(review)
#   corpus.append(review)
#
#
# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(max_features = 1500)
# X = cv.fit_transform(corpus).toarray()
# from sklearn.externals import joblib
# joblib.dump(cv.vocabulary_, "vectorizer.pkl")
#
#
# L = dataset.iloc[:, 1].values
#
# from sklearn.cross_validation import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X, L, test_size = 0)
#
# from sklearn.svm.libsvm import  predict_proba
# from sklearn.linear_model import LogisticRegression
# from sklearn.multiclass import OneVsRestClassifier
#
# anothercorpus = []
# model = OneVsRestClassifier(LogisticRegression())
# model.fit(X_train, Y_train)
#
# from sklearn.externals import joblib
# joblib.dump(model, "model.pkl")
# print "done"

import re
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.svm.libsvm import  predict_proba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

anothercorpus = []
retrieved_model = joblib.load("model.pkl")
retrieved_vectorizer = CountVectorizer(vocabulary = joblib.load("vectorizer.pkl"))

def preprocessing(testvar):
    testing = re.sub('[^a-zA-Z]', ' ', testvar)
    testing = testing.lower()
    testing = testing.split()
    ps = PorterStemmer()
    testing = [ps.stem(word) for word in testing if not word in set(stopwords.words('english'))]
    testing = ' '.join(testing)
    anothercorpus.append(testing)


def predictionFunction():
    global probs1
    global probs11
    probs1 = retrieved_model.predict_proba(R)
    probs11 = retrieved_model.predict(R)
    print(probs11)


testvar = input()
# mode = int(input())
preprocessing(testvar)
# cv = CountVectorizer(max_features = 1500)
R = retrieved_vectorizer.transform(anothercorpus).todense()
predictionFunction()
