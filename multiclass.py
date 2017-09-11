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

Main_Path = "/home/neil/Desktop/fearanalysis"
os.chdir(Main_Path)

dataset = pd.read_csv('what.csv', delimiter='\t', quoting=3, sep=';')
dataset_water = pd.read_csv('what.csv', delimiter='\t', quoting=3, sep=';')
dataset_heights = pd.read_csv('what.csv', delimiter='\t', quoting=3, sep=';')
dataset_rejection = pd.read_csv('what.csv', delimiter='\t', quoting=3, sep=';')
dataset_lonliness = pd.read_csv('what.csv', delimiter='\t', quoting=3, sep=';')
import re
import nltk
import sklearn
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

number_of_classes = 5

corpus = []
corpus_water = []
corpus_heights = []
corpus_rejection = []
corpus_lonliness = []

for i in range(0, 1000):
  review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus.append(review)

  review = re.sub('[^a-zA-Z]', ' ', dataset_water['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus_water.append(review)

  review = re.sub('[^a-zA-Z]', ' ', dataset_heights['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus_heights.append(review)

  review = re.sub('[^a-zA-Z]', ' ', dataset_rejection['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus_rejection.append(review)

  review = re.sub('[^a-zA-Z]', ' ', dataset_lonliness['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus_lonliness.append(review)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
X_water = cv.fit_transform(corpus_water).toarray()
X_heights = cv.fit_transform(corpus_heights).toarray()
X_rejection = cv.fit_transform(corpus_rejection).toarray()
X_lonliness = cv.fit_transform(corpus_lonliness).toarray()
"""y = dataset.iloc[:, 1].values
Y = dataset.iloc[:, 2].values
Z = dataset.iloc[:, 3].values
W = dataset.iloc[:, 4].values
P = dataset.iloc[:, 5].values"""
L = dataset.iloc[:, 6].values
L_water = dataset_water.iloc[:, 6].values
L_heights = dataset_heights.iloc[:, 6].values
L_rejection = dataset_rejection.iloc[:, 6].values
L_lonliness = dataset_lonliness.iloc[:, 6].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, L, test_size = 0.001)
X_train_water, X_test_water, Y_train_water, Y_test_water = train_test_split(X_water, L_water, test_size = 0.001)
X_train_heights, X_test_heights, Y_train_heights, Y_test_heights = train_test_split(X_heights, L_heights, test_size = 0.001)
X_train_rejection, X_test_rejection, Y_train_rejection, Y_test_rejection = train_test_split(X_rejection, L_rejection, test_size = 0.001)
X_train_lonliness, X_test_lonliness, Y_train_lonliness, Y_test_lonliness = train_test_split(X_lonliness, L_lonliness, test_size = 0.001)
#X_train3, X_test3, W_train, W_test = train_test_split(X, L, test_size = 0.001)
#X_train4, X_test4, P_train, P_test = train_test_split(X, L, test_size = 0.001)

# Fitting Naive Bayes to the Training set
"""from sklearn.naive_bayes import GaussianNB
from sklearn import svm"""
from sklearn.svm.libsvm import  predict_proba
#from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
probss = []
anothercorpus = []
model = OneVsRestClassifier(LogisticRegression())
model.fit(X_train, y_train)
model_water = OneVsRestClassifier(LogisticRegression())
model_water.fit(X_train_water, Y_train_water)
model_heights = OneVsRestClassifier(LogisticRegression())
model_heights.fit(X_train_heights, Y_train_heights)
model_rejection= OneVsRestClassifier(LogisticRegression())
model_rejection.fit(X_train_rejection, Y_train_rejection)
model_lonliness = OneVsRestClassifier(LogisticRegression())
model_lonliness.fit(X_train_lonliness, Y_train_lonliness)
#results = model.predict_proba(X_test)[0]

agg1 = np.empty([1,5])
agg2 = np.empty([1,5])
agg3 = np.empty([1,5])
#print(testvar)
#print(mode)

def preprocessing(testvar):
    testing = re.sub('[^a-zA-Z]', ' ', testvar)
    testing = testing.lower()
    testing = testing.split()
    ps = PorterStemmer()
    testing = [ps.stem(word) for word in testing if not word in set(stopwords.words('english'))]
    testing = ' '.join(testing)
    anothercorpus.append(testing)
    #from sklearn.feature_extraction.text import CountVectorizer
    #vect = CountVectorizer()

    #Y = X.toarray()


def predictionFunction(mode):
    global probs1
    global probs11
    if mode == 1:
        probs1 = model.predict_proba(R)
        probs11 = model.predict(R)
        print(probs11)

    if mode == 2:
        probs1 = model_water.predict_proba(R)
        probs11 = model_water.predict(R)
        print(probs11)

    if mode == 3:
        probs1 = model_heights.predict_proba(R)
        probs11 = model_heights.predict(R)
        print(probs11)

    if mode == 4:
        probs1 = model_rejection.predict_proba(R)
        probs11 = model_rejection.predict(R)
        print(probs11)

    if mode == 5:
        probs1 = model_lonliness.predict_proba(R)
        probs11 = model_lonliness.predict(R)
        print(probs11)

a = 5
while a>0:
    testvar = input()
    mode = int(input())
    preprocessing(testvar)
    R = cv.transform(anothercorpus).todense()
    predictionFunction(mode)
    a = a - 1

#print (probs1)
#print(probs11)
x=0
while x<5:
    print(probs11[x])
    agg2[x] = (probs11[x]/(sum(probs11)))*10
    agg3[x] = agg2[x]*20
    agg2[x] = np.floor(agg2[x])
    x = x + 1
#print(agg2)

print("aggregate classes for each fear")
for x in range(0,len(agg1)):
    print(agg2[x], agg3[x])
    print("\n")
    #print("\n")

#if (mode == 1):
 #   print("hi mode is 1")
# great food, great ambience. service was a little slow but would still recommend this place to everyone i know
# The food was extremely delicious but the service was slow and inefficient
