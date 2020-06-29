# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:27:12 2020

@author: qtckp
"""

from itertools import zip_longest
import re


def remove_urls (vTEXT):
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|-)*', '', vTEXT, flags=re.MULTILINE)

def get_ngrams(arr, n=2):
    """
    Делает n-grams из набора слов.
    Аналогичный метод из TextBlob почему-то автоматом ещё удалаяет символы типа # 
    """
    if len(arr)<n:
        yield []
    if len(arr) == n:
        yield arr
    
    for k in range(n,len(arr)+1):
        yield arr[(k-n):k]


def get_sentences(txt):
    """
    Разбивает текст на предложения, учитывая, что фразы типа "мат. алгоритмы", "и т. д.", ".NET" --- это всё одно предложение 
    """
    
    inds = []
    
    for i in range(len(txt)):
        if txt[i] == '.':
            if i+1 == len(txt):
                inds.append(i+1)
            elif txt[i+1].isspace():
                #print(txt[i+2])
                #print(txt[i+2].islower())
                if i+2 < len(txt) and (not txt[i+2].islower() or txt[i+2]=='.'):
                    inds.append(i+1)
    
    #print(inds)
    #print([txt[i-1] for i in inds])
    if len(inds)>0:
        return [txt[i:j-1] for i,j in zip_longest([0]+inds[:-1], inds)]
    return [txt]                
        
        
        
if __name__ == '__main__':
    
    text = "Я люблю мат. алгоритмы, мат. физику. И я не пиздабол. . Это точно."
    print(get_sentences(text))
    
    
    urls = [
        'https://www.kaggle.com/demetrypascal',
        'https://github.com/PasaOpasen/MathClasses',
        'https://github.com/PasaOpasen/Old_Math_Projects',
        'https://github.com/PasaOpasen/Powerlifting-training-diary-and-articles',
        'https://github.com/PasaOpasen/Search-for-defects-in-plates',
        'https://github.com/PasaOpasen/PersianG2Pbot',
        'https://www.litres.ru/demetriy-paskal/',
        'https://elibrary.ru/item.asp?id=38189363',
        'https://www.linkedin.com/in/dmitry-pasko-5bb57219b/',
        'https://stackoverflow.com/users/13119067/Дмитрий-Пасько',
        ]
    
    for u in urls:
        print(f'{u} --> {remove_urls(u)}')















