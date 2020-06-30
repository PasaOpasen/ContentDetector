# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:47:43 2020

@author: qtckp
"""

import textblob as tb

langs=[]
for gg in g:
    
    if len(gg)<3:
        langs.append('small')
    else:
        blob = tb.TextBlob(gg)
        try:
            langs.append(blob.detect_language())
        except:
            langs.append('dunno')
   
     
for gg, l in zip(g, langs):
    print(f'{gg}    {l}')
