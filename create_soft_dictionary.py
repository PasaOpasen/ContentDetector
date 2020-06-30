# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:12:02 2020

@author: qtckp
"""


import os 
import io
from stemmer_rus import Stem_text
import json

if __name__ == '__main__':
    dr = os.path.dirname(__file__)
    
    _from = os.path.join(dr, 'soft_skills.txt')
    
    with io.open(_from,'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    
    voc = {}
    for line in lines:
        if '|' in line:
            i = line.index('|')
            arr = line[:i].rstrip().split(',')
            val = line[i+1:].strip()
            for w in arr+[val]:
                voc[' '.join(list(Stem_text(w.lower())))] = val
        else:
            voc[' '.join(list(Stem_text(line.lower())))] = line[:-1]
        
    #voc = {' '.join(list(Stem_text(text.lower()))): text[:-1] for text in lines}

    #print(voc)
    _to = os.path.join(dr, 'soft_skills.json')
    
    with io.open(_to,'w', encoding = 'utf-8') as f:
        json.dump(voc, f, indent=4)
    
    #print(dr)


