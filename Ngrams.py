# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:11:56 2020

@author: qtckp
"""


import textblob as tb
import io
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import sys


def print_list(lst):
    for r in lst:
        print(r)
    print()
    print()
    print()

def remove_urls (vTEXT):
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)

def get_ngrams(arr, n=2):
    if len(arr)<n:
        yield []
    if len(arr) == n:
        yield arr
    
    for k in range(n,len(arr)+1):
        yield arr[(k-n):k]




def txt_list_to_grams(lines, debug = 1, out_file = 'report.txt'):
        
    if debug:
        file = open(out_file,'w')
        sys.stdout = file
        
        print('BEGIN:')
        print_list(lines)
    
    
    
    # 2) filter and delete garbage
    
    # delete empty lines
    lines = filter( lambda l: len(l)>0, (line.strip() for line in lines))
    
    if debug:
        lines=list(lines)
        print('DELETE EMPTY LINES')
        print_list(list(lines))
    
    # remove urls
    lines = map(remove_urls, lines)
    
    if debug:
        lines = list(lines)
        print('DELETE URLS')
        print_list(lines)
    
    
    # replace strange symbols with space
    convert = lambda s: s if s in ['.','#','+'] or s.isspace() or s.isalnum() else ' '
    
    lines = (
        ''.join((convert(s) for s in line)).strip() 
        for line in lines)
    
    if debug:
        lines=list(lines)
        print('DELETE STRANGE SYMBOLS')
        print_list(list(lines))
    
    # delete multiple spaces
    lines = [' '.join(line.split()) for line in lines]
    
    if debug:
        print('DELETE MULTIPLE SPACES')
        print_list(list(lines))
    
    
    # можно еще поисправлять ошибки и т п, но это не так просто
    
    
    # 3) detect sentences
    
    sentences = []
    
    for obj in lines:
        sentences += [str(sent) for sent in tb.TextBlob(obj).sentences] 
    
    if debug:
        print('SPLIT BY SENTENCES')
        print_list(sentences)
    
    # remove stopwords
    
    sentences = [' '.join([w for w in s.split() if w not in stopwords.words('english')]) for s in sentences]
    sentences = [' '.join([w for w in s.split() if w not in stopwords.words('russian')]) for s in sentences]
    
    if debug:
        print('REMOVE STOP WORDS')
        print_list(sentences)
    
    # split by n-grams
    
    ngrams = list( 
        set().union(*[ 
            #[' '.join(list(g)) for g in tb.TextBlob(txt).ngrams(2)] 
            [' '.join(list(g)) for g in get_ngrams(txt.split(), 2)] 
            for txt in sentences]).union(*[ 
            [' '.join(list(g)) for g in get_ngrams(txt.split(), 1)] for txt in sentences])
        )
    
    if debug:
        ngrams = list(ngrams)
        print('GET 1/2 NGRAMS')
        print_list(ngrams)
    
    
    # delete ngrams without alpha
    
    ngrams = [g for g in ngrams if len(g)>1 and any((s.isalpha() for s in g))]
    
    if debug:
        print('DELETE NGRAMS WITHOUT ALPHA')
        print_list(ngrams)
    
    
    # delete bad symbols in beginning
    symbs = [s for s in set().union(*ngrams) if not s.isalnum()]
    
    try: # for .NET
        symbs.remove('.')
    except:
        pass
    
    ngrams = [g.lstrip(''.join(symbs)) for g in ngrams]
    
    if debug:
        print('DELETE SYMBOLS LIKE + # ) FROM LEFT PART OF WORDS')
        print_list(ngrams)
       
    ngrams = list(set(ngrams))
    
    
    if debug:
        print('RESULTS')
        print_list(ngrams)
        file.close()
    
    return ngrams
    
    
if __name__=='__main__':
    
    # 1) read file
    
    with io.open('my_resume.txt','r', encoding = 'utf-8') as f:
        doclines = f.readlines()
    
    original_stdout = sys.stdout
    g = txt_list_to_grams(doclines,1)
    
        
    sys.stdout = original_stdout
        
