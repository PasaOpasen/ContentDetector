# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:20:22 2020

@author: qtckp
"""


import sys, os, io
sys.path.append(os.path.dirname('../'))

from content_detector.create_graph_dictionary import Graph
from content_detector.detector import get_content_from_text
import content_detector.stemmer_rus# import update_dictionary
import numpy as np


from termcolor import colored
import colorama

voc = None

def update_graph():
    print('updating...')
    Graph.update_graph()
    #update_dictionary()
    global voc
    voc = content_detector.stemmer_rus.get_stem_dictionary()






with open('vacs.csv','r', encoding = 'utf8') as f:
    lines = [line.split(';') for line in f.readlines()]
    
lines = [(line[0],line[1]) for line in lines[1:] if line[0] != 'NA']




inds = np.arange(len(lines))
np.random.shuffle(inds)


i=0

while i < inds.size:
    indx = inds[i]
    l1 = lines[indx][0]
    l2 = lines[indx][1]
    res1 = get_content_from_text([l1], False, voc)
    res2 = get_content_from_text([l2], False, voc)
    
    print(colored(f'key = {l1}', on_color = 'on_blue'))
    print(colored(f'skills = {res1}', on_color = 'on_green'))
    print()
    print(l2)
    print(colored(f'{res2}', on_color = 'on_cyan'))
    
    
    tmp = input('press + for continue and something else for reload: ')
    print()
    if tmp == '+':
        i +=1
    else:
        update_graph()
        print()
    
    

