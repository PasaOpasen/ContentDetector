# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:03:31 2020

@author: qtckp
"""


import itertools
import collections

def levenshtein_distance(string1, string2):
       """
       >>> levenshtein_distance('AATZ', 'AAAZ')
       1
       >>> levenshtein_distance('AATZZZ', 'AAAZ')
       3
       """

       distance = 0

       if len(string1) < len(string2):
           string1, string2 = string2, string1

       for i, v in itertools.zip_longest(string1, string2, fillvalue='-'):
           if i != v:
               distance += 1
       return distance

def levenshtein_distance_better(s1,s2, remove_desc = True):
    """
    Возвращается наименьшее расстояние левенштейна среди разных комбинаций case и с поправкой на скобки
    """
    if remove_desc and '(' in s2:
        s2 = s2[:s2.index('(')].rstrip()
    
    tmp = [
        levenshtein_distance(s1, s2),
        levenshtein_distance(s1.lower(), s2),
        levenshtein_distance(s1.upper(), s2),
        levenshtein_distance(s1.title(), s2)
        ]
    if ' ' in s1:
        tmp.append(levenshtein_distance(s1.capitalize(), s2))
    
    return min(tmp)





if __name__ == '__main__':
    
    pairs = [
        ('r', "R (Programming language)"),
        ('.net', '.NET')
        ]
    for a, b in pairs:
        
        print(f"{a} | {b} ---> {levenshtein_distance_better(a, b)}")















