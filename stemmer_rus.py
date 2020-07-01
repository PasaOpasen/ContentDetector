# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:04:07 2020

@author: qtckp
"""

import Stemmer
import os, json, io

stemmer = Stemmer.Stemmer('russian')

def Stem_text(text):
    return set(stemmer.stemWords(text.lower().split()))

def get_stem_dictionary():
    dr = os.path.dirname(__file__)
    with io.open(os.path.join(dr, 'soft_skills.json'),'r', encoding = 'utf-8') as f:
        r = json.load(f)
    print(r)
    return r

def get_soft_skills(grams):
    
    full = set()
    for g in grams:
        full=full.union(Stem_text(g))
    
    voc = get_stem_dictionary()
    
    result = []
    for key, value in voc.items():
        if set(key.split()).issubset(full):
            if type(value) == list:
                result+=value
            else:
                result.append(value)
    return list(set(result))




