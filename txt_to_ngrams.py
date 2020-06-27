# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:30:10 2020

@author: qtckp
"""


import textblob as tb
import io
import re


def print_list(lst):
    for r in lst:
        print(r)

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


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


# split by n-grams

ngrams = list( 
    set().union(*[ 
        [' '.join(list(g)) for g in tb.TextBlob(txt).ngrams(2)] 
        for txt in sentences])
    )


print_list(ngrams)

# give to ...


