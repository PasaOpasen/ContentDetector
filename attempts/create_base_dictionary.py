# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:16:50 2020

@author: qtckp
"""

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from prepare_functions import RUSSIAN_SYMBOLS

if __name__ == '__main__':
    
    dc = list(set(
    stopwords.words('russian') + # russian stop words
            stopwords.words('english') + 
            RUSSIAN_SYMBOLS + # only one russian symbols
            ['в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при', 'через', 'с', 'у', 'за', 'над', 'об', 'под', 'про', 'для'] # предлоги
            ))
    
    with open('stopwords(default).txt', 'w') as f:
        f.writelines([w+'\n' for w in dc])




