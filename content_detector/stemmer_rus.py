# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:04:07 2020

@author: qtckp
"""

import Stemmer
import os, json, io

stemmer = Stemmer.Stemmer('russian')



def Get_dictionary_values():
    return list(set(dictionary.keys()))

def Stem_text(text):
    return set(stemmer.stemWords(text.lower().split()))

def get_stem_dictionary(filename = 'graph_skills.json'):
    """
    'graph_skills.json'
    'soft_skills.json'
    """
    dr = os.path.dirname(__file__)
    with io.open(os.path.join(dr, filename),'r', encoding = 'utf-8') as f:
        r = json.load(f)
    #print(r)
    return r

dictionary = get_stem_dictionary()

def get_soft_skills(grams):
    
    full = set()
    for g in grams:
        full=full.union(Stem_text(g))
    
    voc = dictionary
    
    result = []
    for key, value in voc.items():
        if set(key.split()).issubset(full):
            if type(value) == list:
                result+=value
            else:
                result.append(value)
    return list(set(result))

def get_soft_skills2(s_grams, h_grams, vocab = dictionary):
    """
    работает как get_soft_skills(s_grams + h_grams),
    но удаляет лишнее из h_grams
    """
    
    full = set()
    for g in s_grams + h_grams:
        full=full.union(Stem_text(g))
    #print(full)
    voc = vocab
    
    result = []
    result_set = set()
    for key, value in voc.items():
        st = set(key.split())
        if st.issubset(full):
            result_set = result_set.union(st)
            if type(value) == list:
                result+=value
            else:
                result.append(value)
          
    inds = []
    for i in range(len(h_grams)):
        if Stem_text(h_grams[i]).issubset(result_set):
            inds.append(i)
    
    for i in inds[::-1]:
        del h_grams[i]
    
    return list(set(result))


def update_dictionary():
    global dictionary
    dictionary = get_stem_dictionary()

