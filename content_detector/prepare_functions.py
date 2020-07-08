# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:27:12 2020

@author: qtckp
"""

from itertools import zip_longest
import re

RUSSIAN_SYMBOLS = list('АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя')

def has_more_than_x_russian_symbols(text, mincount = 2):
    """
    Does text contain at least mincount russian symbols?
    """
    t = 0
    for s in RUSSIAN_SYMBOLS:
        if s in text:
            t+=1
            if t == mincount:
                return True
    return False
    

def remove_urls (vTEXT):
    return re.sub(r'((https|http)?:\/\/|www\.)(\w|\.|\/|\?|\=|\&|\%|-)*', '', vTEXT, flags=re.MULTILINE)

def remove_mails(text):
    return re.sub(r"\S*@\w*\.\w*(\s?|,|\.)",'',text)

def remove_bots(text):
    return re.sub(r"\@[\w\d]*",'',text)


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
        return [txt[i:j-1] for i,j in zip_longest([0]+inds[:-1], inds)] + [txt[inds[-1]+1:]]
    return [txt]                
        


def split_by_words(sentence, words, lst =[]):
    
    splitlist = sentence.split()
    
    flag = True
    for word in words:
        if word in splitlist:
            #print(word)
            ind = sentence.index(word)
            split_by_words(sentence[:ind], words, lst)
            split_by_words(sentence[ind+len(word):], words,lst)
            
            flag = False
            break
    if flag:
        lst.append(sentence)


def split_by_words2(sentence, words):
    """
    Делает split предложения по stopwords
    """
    result = []
    tmp=[]
    for w in sentence.split():
        if w in words:
            if len(tmp)>0:
                result.append(' '.join(tmp))
                tmp=[]
        else: 
            tmp.append(w)
    
    if len(tmp)>0:
        result.append(' '.join(tmp))
    
    return result

        
if __name__ == '__main__':
    
    text = "Я люблю мат. алгоритмы, мат. физику. И я не пиздабол. . Это точно."
    print(get_sentences(text))
    
    text = "Мы ищем опытного Android разработчика для разработки мобильной версии проекта по управлению жизненным циклом зданий. Требования Опыт создания Android приложений от 3 лет Хорошее знание методологии ООП Понимание принципов работы сервисно ориентированной архитектуры Знание паттернов проектирование и умение их применять Желательно хорошее знание английского языка Большим плюсом будет наличие примеров работ Условия Трудоустройство согласно ТК РФ Стабильная высокая белая заработная плата зависит от уровня мастерства кандидата и обсуждается индивидуально при собеседовании Гибкий график работы Возможность работы как в офисе"
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
        'www.behance.net/umkabear'
        ]
    
    for u in urls:
        print(f'{u} --> {remove_urls(u)}')
        
        
        
    sentence = 'one two three 4 5 six seven 8 nine'
    words = ['two', '5','nine']
    
    lst = []
    split_by_words(sentence, words, lst)
    print(lst)














