# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:49:31 2020

@author: qtckp
"""
import time
import wikipedia

ngrams_eng=[]
for g in ngrams:
    blob = tb.TextBlob(g)
    if len(g)<3:
        ngrams_eng.append(g)
    elif blob.detect_language() == 'en':
        ngrams_eng.append(g)
    else:
        try:
            print(f'translate {g}')
            ngrams_eng.append(str(blob.translate()))
        except:
            print(f"cannot translate {g}")
            ngrams_eng.append(g)
        time.sleep(2)


obj = [wikipedia.search(n) for n in ngrams]

for g, o in zip(ngrams,obj):
    print(g)
    print('-------')
    print(o)
    print()
    
    










for g, o in zip(ngrams,obj):
    if g.lower() in (w.lower() for w in o):
        print(g.title())





import itertools
import collections
def levenshtein_distance(string1, string2):
       """
       >>> levenshtein_distance('AATZ', 'AAAZ')
       1
       >>> levenshtein_distance('AATZZZ', 'AAAZ')
       3
       """

       distance = 0

       if len(string1) < len(string2):
           string1, string2 = string2, string1

       for i, v in itertools.zip_longest(string1, string2, fillvalue='-'):
           if i != v:
               distance += 1
       return distance


for g, o in zip(ngrams,obj):
    
    low = g.lower()
    dists = [(w,levenshtein_distance(low, w.lower())) for w in o]
    
    betters = [(w,l) for (w,l) in dists if l<10 and l<len(g)]
    
    if len(betters)>0:
        print(g)
        print('-------')
        print(betters)
        print()





