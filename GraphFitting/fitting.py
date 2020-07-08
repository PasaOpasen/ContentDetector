# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:20:22 2020

@author: qtckp
"""













with open('vacs.csv','r', encoding = 'utf8') as f:
    lines = [line.split(';') for line in f.readlines()]
    
lines = [(line[0],line[1]) for line in lines[1:] if line[0] != 'NA']






