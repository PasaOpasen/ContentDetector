# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:27:19 2020

@author: qtckp


пришёл к тому, что можно контролировать верхнюю границу времени ожидания (но этого не нужно)

можно менять дефолтный язык. это может принести пользу в некоторых случаях, но хз как такие случаи определять дальше
+ это может выйти боком при развертывании, так там глобальная установка
(если надо, клонирую репозиторий и исправлю)

"""

import sys
sys.path.append('../')



from Ngrams import txt_list_to_grams
from prepare_functions import *
import io
import wikipedia
import time


#from datetime import timedelta
#wikipedia.set_rate_limiting(True, min_wait=timedelta(milliseconds=50))


with io.open('../my_resume.txt','r', encoding = 'utf-8') as f:
        doclines = f.readlines()
    
grams = txt_list_to_grams(doclines,0)


h = []
s = []
      
for g in grams:
    if has_more_than_x_russian_symbols(g,2):
        s.append(g)
    else:
        h.append(g)


for gram in h:#['майкрософт','май кросовок', 'майкрасофт', 'майнкрафт']:
    print()
    print(gram)
    print('--------------')
    
    start = time.time()
    w = wikipedia.search(gram)
    end = time.time()
    print(f'just search :{end - start}')

    start = time.time()
    ww = wikipedia.search(gram, results = 5)
    end = time.time()
    print(f'search only 5 :{end - start}')

    start = time.time()
    ww = wikipedia.suggest(gram)
    end = time.time()
    print(f'suggest :{end - start}')
    
    print(w)
    
   
    
#wikipedia.set_lang('ru')    

r = []
for gram in s:
    w = wikipedia.search(gram, results = 1)
    if len(w)>0:
        r.append(w[0])
        



