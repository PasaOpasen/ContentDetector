# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:31:32 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname('../'))
from content_detector.stemmer_rus import Stem_text
import numpy as np



with open('vacs_experience.csv','r', encoding = 'utf8') as f:
    lines = [line.split(';') for line in f.readlines()]


lines = [(line[0].strip(),line[1].strip()) for line in lines[1:] if line[0] != 'NA']

voc = {
       'Нет опыта':0,
       'От 1 года до 3 лет':1,
       'От 3 до 6 лет':2,
       'Более 6 лет':3
       }

p = [
     ['опыт','опыта'],
     ['год','лет'],
     ['желателен','желательно'],
     ['необходимо','обязательно','обязателен' ],
     ['один', 'одного'],
     ['два','двух'],
     ['три', 'трех'],
     ['четыре','четырех'],
     ['пять', 'пяти'],
     ['шесть', 'шести']
     ]

pp = []#[Stem_text(txt) for line in p  for txt in line]

for line in p:
    pp.append([Stem_text(txt) for txt in line])



X = []
y = []

for line in lines:
    a, b = line
    b = "".join([s for s in b if s.isalnum() or s.isspace()])
    b = Stem_text(b)
    
    pps = [ any((t.issubset(b) for t in line))  for line in pp]
    
    lst =  [str(i) in b for i in range(1,12)]
    
    #print(b)
   # print(lst)    
    
    y.append(voc[a])
    X.append(pps+lst)


y = np.array(y)
X = np.array(X)

X.sum(axis=0)





import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn import linear_model
import sklearn







names = [
    #"Nearest Neighbors", 
      # "Linear SVM", 
     #  "RBF SVM", 
     #  'poly svm',
       # 'sigmoid svm',
        'sgd',
        "Decision Tree", 
        "Random Forest", 
       "Neural Net", 
        "AdaBoost",
        # "Naive Bayes gau",

         #"QDA",
         'logreg',
         'ridge',
         'boost'
         ]


classifiers = [
  # KNeighborsClassifier(5),
  # LinearSVC(C=1,verbose=1),
   # SVC(gamma=2, C=1,verbose=True),
   # SVC(kernel='poly'),
   # SVC(kernel='sigmoid'),
    SGDClassifier(),
    DecisionTreeClassifier(max_depth=8),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1,verbose=True),
   MLPClassifier(alpha=1, max_iter=1000,verbose=True),
   AdaBoostClassifier(),
  # GaussianNB(),

    #QuadraticDiscriminantAnalysis() ,
    LogisticRegression(),
    linear_model.RidgeClassifier(alpha=0.1),
    sklearn.ensemble.GradientBoostingClassifier()
    ]




X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=.2, train_size=.1, shuffle = True )



for name, clf in zip(names, classifiers):
    print('Now: {}'.format(name))
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    #f1 = f1_score(y_test, clf.predict(X_test))
    print(classification_report(y_test, clf.predict(X_test), digits = 7))
    print("model = {}  score = {}".format(name,score))




from sklearn.model_selection import GridSearchCV

params = [{
    'max_depth':[2,3,4,5,6,7,8,9,10],
    'n_estimators':[10,20,30,40,50],
    'max_features':[1,2,3,4,5,6,7,8],
           }]
clf= RandomForestClassifier()

gr= GridSearchCV(clf,params,cv=5,verbose=1, n_jobs = -1)

gr.fit(X_train, y_train)

gr.cv_results_











