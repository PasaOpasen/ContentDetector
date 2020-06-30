# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:29:46 2020

@author: qtckp
"""

from prepare_functions import *


# для английского
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer 
# Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()
# Lemmatize Single Word
print(lemmatizer.lemmatize("bats"))
#> bat
print(lemmatizer.lemmatize("are"))
#> are
print(lemmatizer.lemmatize("feet"))
#> foot

print(lemmatizer.lemmatize(".NET"))

print(lemmatizer.lemmatize("мыши"))




import Stemmer

stemmer = Stemmer.Stemmer('russian')

print(stemmer.stemWords(['схожим', 'основные']))



# для русского

from pymystem3 import Mystem
text = "Красивая мама красиво мыла раму"
m = Mystem()
lemmas = m.lemmatize(text)
print(''.join(lemmas))





import rutokenizer
import rupostagger
import rulemma


lemmatizer = rulemma.Lemmatizer()
lemmatizer.load()

tokenizer = rutokenizer.Tokenizer()
tokenizer.load()

tagger = rupostagger.RuPosTagger()
tagger.load()

sent = u'Мяукая, голодные кошки ловят жирненьких хрюнделей'
tokens = tokenizer.tokenize(sent)
tags = tagger.tag(tokens)
lemmas = lemmatizer.lemmatize(tags)
for word, tags, lemma, *_ in lemmas:
	print(u'{:15}\t{:15}\t{}'.format(word, lemma, tags))










for gr in g:
    if has_more_than_x_russian_symbols(gr,2):
        #l = ''.join(m.lemmatize(gr)[:-1])
        l = stemmer.stemWords(gr.lower().split())
        print(f'{gr} ---> {l}')




stemmer.stemWords(['грамотный','английский','ООП'])











