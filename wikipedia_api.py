# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:49:31 2020

@author: qtckp
"""
import io
import re
import time
import wikipedia
from detect_functions import levenshtein_distance_better, levenshtein_distance
from Ngrams import txt_list_to_grams, print_list
import numpy as np



with io.open('my_resume.txt','r', encoding = 'utf-8') as f:
    doclines = f.readlines()
    
ngrams = txt_list_to_grams(doclines,0)
              
print_list(ngrams)



def print_pairs_list(l1, l2):
    for g, o in zip(l1,l2):
        print(g)
        print('-------')
        print(o)
        print()


# ngrams_eng=[]
# for g in ngrams:
#     blob = tb.TextBlob(g)
#     if len(g)<3:
#         ngrams_eng.append(g)
#     elif blob.detect_language() == 'en':
#         ngrams_eng.append(g)
#     else:
#         try:
#             print(f'translate {g}')
#             ngrams_eng.append(str(blob.translate()))
#         except:
#             print(f"cannot translate {g}")
#             ngrams_eng.append(g)
#         time.sleep(2)


obj = [wikipedia.search(n) for n in ngrams]

print_pairs_list(ngrams, obj)
    
    


for g, o in zip(ngrams,obj):
    if g.lower() in (w.lower() for w in o):
        print(g.title())



for g, o in zip(ngrams,obj):
    
    dists = [(w,levenshtein_distance_better(g, w)) for w in o]
    
    betters = [(w,l) for (w,l) in dists if l<6 and l<len(g)]
    
    if len(betters)>0:
        print(g)
        print('-------')
        print(betters)
        print()



def clean_list(arr):
    
    if len(arr)==0:
        return arr
    
    res = sorted(list(set(arr)))
    
    deleted = []
    
    reg = r"\d+"
    
    for i in range(len(res)-1):
        for j in range(i+1,len(res)):
            if i not in deleted and j not in deleted:
                
                ri, rj = res[i].lower(), res[j].lower()
                
                #print(f"{ri} | {rj}")
                
                if ri in re.sub(reg,'', rj).split():# это нужно, чтобы убрать всякие C7 и т. п.
                    if re.search(reg, rj):
                        print(f"1) {ri} | {rj}")
                        deleted.append(j)
                    else:
                        print(f"2) {ri} | {rj}")
                        deleted.append(i)
                elif rj in re.sub(reg,'', ri).split():
                    if re.search(reg, ri):
                        print(f"3) {ri} | {rj}")
                        deleted.append(i)
                    else:
                        print(f"4) {ri} | {rj}")
                        deleted.append(j)

    
    for i in sorted(deleted, reverse = True):
        del res[i]
        
    return res
    

def get_skills(grams, descriptions):
    
    result = []
    
    for g, o in zip(grams,descriptions):
        
        dists = [(w,levenshtein_distance_better(g, w)) for w in o]
        
        betters = [(w,l) for (w,l) in dists if l<6 and l<len(g)]
        
        if len(betters)>0:
            if len(betters) == 1:
                result.append(betters[0][0])
            else:
                #count_of_zero = len((l for _, l in betters if l == 0))
                
                words, counts = zip(*betters)
                counts = np.array(counts, dtype = 'int16')
                count_of_zero = np.sum(counts == 0)
                
                if count_of_zero < 2:
                    result.append(words[counts.argmin()])
                else:
                    counts = np.array((levenshtein_distance_better(g,w) for w in words))
                    result.append(words[counts.argmin()])           
    
    return clean_list(result)


r = get_skills(ngrams, obj)
print_list(r)
