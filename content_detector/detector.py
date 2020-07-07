# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:20:38 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname(__file__))

from Ngrams import txt_list_to_grams

from stemmer_rus import Get_dictionary_values, Stem_text, get_soft_skills2

from wikipedia_api import get_hard_skills

from prepare_functions import *



def get_content_from_text(lines_of_text, use_wiki = True):
    
    grams = txt_list_to_grams(lines_of_text,0)
    #print(grams)
    
    h = []
    
    s = []
    
    for g in grams:
        if has_more_than_x_russian_symbols(g,2):
            s.append(g)
        else:
            h.append(g)
    #print(s);print(h)
    soft_skills = get_soft_skills2(s, h)
    
    if len(h)>0 and use_wiki:
    
        hard_skills = get_hard_skills(h)
    
        soft_skills_lower = [word.lower() for word in soft_skills]
        
        h = [answer for answer in hard_skills if answer.lower() not in soft_skills_lower]
        
        return soft_skills + h
    
    return soft_skills



if __name__=='__main__':
    
    
    with io.open("0.txt",'r', encoding = 'utf-8') as f:
        doclines = f.readlines()
        
    answer = get_content_from_text(doclines)
    print(answer)
    
    

