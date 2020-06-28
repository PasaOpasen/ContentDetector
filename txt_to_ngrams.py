# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:30:10 2020

@author: qtckp
"""


import textblob as tb
import io
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


def print_list(lst):
    for r in lst:
        print(r)

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

def get_ngrams(arr, n=2):
    if len(arr)<n:
        yield []
    if len(arr) == n:
        yield arr
    
    for k in range(n,len(arr)+1):
        yield arr[(k-n):k]





# 1) read file

with io.open('my_resume.txt','r', encoding = 'utf-8') as f:
    lines = f.readlines()
    

# 2) filter and delete garbage

# delete empty lines
lines = filter( lambda l: len(l)>0, (line.strip() for line in lines))

# remove urls
lines = map(remove_urls, lines)

# replace strange symbols with space
convert = lambda s: s if s in ['.','#','+'] or s.isspace() or s.isalnum() else ' '

lines = (
    ''.join((convert(s) for s in line)).strip() 
    for line in lines)


# delete multiple spaces
lines = [' '.join(line.split()) for line in lines]

print_list(lines)


# можно еще поисправлять ошибки и т п, но это не так просто


# 3) detect sentences

sentences = []

for obj in lines:
    sentences += [str(sent) for sent in tb.TextBlob(obj).sentences] 


print_list(sentences)

# remove stopwords

sentences = [' '.join([w for w in s.split() if w not in stopwords.words('english')]) for s in sentences]
sentences = [' '.join([w for w in s.split() if w not in stopwords.words('russian')]) for s in sentences]


# split by n-grams

ngrams = list( 
    set().union(*[ 
        #[' '.join(list(g)) for g in tb.TextBlob(txt).ngrams(2)] 
        [' '.join(list(g)) for g in get_ngrams(txt.split(), 2)] 
        for txt in sentences]).union(*[ 
        [' '.join(list(g)) for g in get_ngrams(txt.split(), 1)] for txt in sentences])
    )


print_list(ngrams)


# delete ngrams without alpha

ngrams = [g for g in ngrams if len(g)>1 and any((s.isalpha() for s in g))]

print_list(ngrams)


# delete bad symbols in beginning
symbs = [s for s in set().union(*ngrams) if not s.isalnum()]

try: # for .NET
    symbs.remove('.')
except:
    pass

ngrams = [g.lstrip(''.join(symbs)) for g in ngrams]

print_list(ngrams)




ngrams = list(set(ngrams))


#from nltk.tokenize import word_tokenize 

#for w in ngrams:
#    print(w)
#    print(word_tokenize(w))


# give to ...




















