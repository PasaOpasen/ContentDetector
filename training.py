# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:02:53 2020

@author: qtckp
"""

import sys, os, io

from Ngrams import txt_list_to_grams, print_list

from stemmer_rus import get_soft_skills, Get_dictionary_values, Stem_text, get_soft_skills2

from wikipedia_api import get_hard_skills

from prepare_functions import *


my_dir = os.path.dirname(__file__)

files = [os.path.join(my_dir,'train_samples',f'{i}.txt') for i in range (0,25)]


if __name__=='__main__':
    
    
    with io.open(files[21],'r', encoding = 'utf-8') as f:
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
            
    #soft_skills = get_soft_skills(s+h)
    
    soft_skills = get_soft_skills2(s,h)
    
    # print()
    # keys = Get_dictionary_values()
    # keys_set = set(keys)
    
    # lowers_skills = [k.lower() for k in soft_skills]
    # lowers = [k.lower().split() for k in soft_skills]
    
    # inds = []
    # for i in range(len(h)):
    #     w = h[i].lower()
    #     #w = Stem_text(h[i])
        
    #     if w in lowers_skills or w in keys:
    #         print(f'{w} in {lowers_skills} or keys')
    #         inds.append(i)
    #     #elif set(w.split()).issubset(keys_set):
    #     elif ' '.join(list(Stem_text(w))) in keys_set:    
    #         print(f'{w} is subset')
    #         inds.append(i)
    #     else:
    #         for k in lowers:
    #             for l in k:
    #                 if w == l:
    #                     print(f'{w} in {l} from {k}')
    #                     inds.append(i)
    #                     break
                
    # for i in inds[::-1]:
    #     del h[i]
    
    print()
    print(f'from graph: {soft_skills}')
    print()
    print(f'to wiki: {h}')
    print()
    
    
    hard_skills = get_hard_skills(h); print(f'from wiki: {hard_skills}')
    
    
    
    
    
    

