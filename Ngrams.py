# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:11:56 2020

@author: qtckp
"""


import textblob as tb
import io
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import sys
import re

from prepare_functions import *


def print_list(lst):
    for r in lst:
       print(r)
    
    #print('R' in lst)
    
    print()
    print()
    print()


splitter = list(set(
    stopwords.words('russian') + # russian stop words
            stopwords.words('english') + 
            RUSSIAN_SYMBOLS + # only one russian symbols
            ['в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при', 'через', 'с', 'у', 'за', 'над', 'об', 'под', 'про', 'для'] # предлоги
            ))




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
    convert = lambda s: s if s in [',','.','#','+'] or s.isspace() or s.isalnum() else ' '
    
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
        print_list(lines)
    
    
    commas=[]
    for line in lines:
        commas += line.split(',')
    
    if debug:
        print('SPLIT BY COMMAS')
        print_list(commas)
    
    # можно еще поисправлять ошибки и т п, но это не так просто
    
    
    # 3) detect sentences
    
    sentences = []
    
    for obj in commas:
        #sentences += [str(sent) for sent in tb.TextBlob(obj).sentences] 
        for sentence in get_sentences(obj): # split by .    
            sentences +=  split_by_words2(sentence, splitter) # split by stopwords #get_sentences(obj)
    
    if debug:
        print('SPLIT BY SENTENCES AND STOP WORDS')
        print_list(sentences)
    
    # remove stopwords
    
    sentences = [' '.join([w for w in s.split() 
                           #if w not in splitter 
                           #and 
                           if not re.match(r"[\w\d]\.", w)]) # - т. п. 1. 2. 3.
                 for s in sentences]
    
    if debug:
        print('REMOVE 1. 2. 3. 4. SYMBOLS')
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
    
    ngrams = [g for g in ngrams if len(g)>0 and any((s.isalpha() for s in g))]
    
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
    
    print_list(g)
        
