# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:02:53 2020

@author: qtckp
"""

import sys, os, io

from Ngrams import txt_list_to_grams, print_list

from stemmer_rus import get_soft_skills

from wikipedia_api import get_hard_skills

from prepare_functions import *



if __name__=='__main__':
    
    
    with io.open('my_resume.txt','r', encoding = 'utf-8') as f:
        doclines = f.readlines()
    
    grams = txt_list_to_grams(doclines,0)
        
    print_list(grams)
    
    h = []
    
    s = []
    
    for g in grams:
        if has_more_than_x_russian_symbols(g,2):
            s.append(g)
        else:
            h.append(g)
            
    soft_skills = get_soft_skills(s+h)
    
    
    lowers = [k.lower().split() for k in soft_skills]
    
    inds = []
    for i in range(len(h)):
        w = h[i].lower()
        for k in lowers:
            for l in k:
                if w == l:
                    print(f'{w} in {l} from {k}')
                    inds.append(i)
                    break
            
    for i in inds[::-1]:
        del h[i]
    
    
    #hard_skills = get_hard_skills(h)
            
    
    
    
    
    
    
    

