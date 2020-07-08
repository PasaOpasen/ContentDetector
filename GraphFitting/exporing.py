# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:49:00 2020

@author: qtckp
"""


with open('vacs.csv','r', encoding = 'utf8') as f:
    lines = [line.split(';')[0] for line in f.readlines()]


lines = [line for line in lines[1:] if line != 'NA']


skills = []
for line in lines:
    skills += [word2.strip() 
               for word in line.split('|')
               for word2 in word.split(',')]
    
skills = list(set(skills))







