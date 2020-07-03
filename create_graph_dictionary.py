# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:37:43 2020

@author: qtckp
"""

import io, os
from stemmer_rus import Stem_text
import json



class Graph:
    def __init__(self, filename):
        with io.open(filename, 'r', encoding = 'utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
        lines = filter(lambda line: len(line), lines)
        
        self.nodes = []
        self.counter = 0
        
        for line in lines:
            
            out = line[-1] == '|'
            if out:
                line = line[:-1]
            
            nodes = [arr.split(',') for arr in line.split('|')]
            
            nodes1 = list(set((word.strip() for word in nodes[0])))
            
            if len(nodes) == 1:
                for word in nodes1:
                    self.nodes.append(Node(word, self.counter))
                    self.counter += 1
            else:
                nodes2 = [word.strip() for word in nodes[1]]
                for word in nodes2:
                    if not self.exist_node(word): 
                        self.nodes.append(Node(word, self.counter))
                        self.counter += 1
                        
                names = self.get_numbers_by_names(nodes2)
                for word in nodes1:
                    self.nodes.append(Node(word, self.counter, names, out))
                    self.counter += 1
        self.compile()
                
        
    
    def exist_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return True      
        return False
    
    def get_number_by_name(self, name):
        for i in range(len(self.nodes)):
            if self.nodes[i].name == name:
                return i
        return -1
    
    def get_numbers_by_names(self, names):
        return [self.get_number_by_name(name) for name in names]
    
    def get_names_by_numbers(self, numbers):
        return [self.nodes[i].name for i in numbers]
    
    def print(self):
        for node in self.nodes:
            print(f'key = {node.key}, name = {node.name}, number = {node.number}, connect = {self.get_names_by_numbers(node.withs)} \t out = {node.out}')
            
       
    def compile(self):
        
        def get_content(i):
            result = []
            it = self.nodes[i]
            for number in it.withs:
                result += get_content(number)
            if it.out:
                result.append(it.name)
            return result
        
        
        for i in range(len(self.nodes)):
            self.nodes[i].content = list(set(get_content(i)))
        
    def print_content(self):
        for node in self.nodes:
            print(f'{node.name} --> {node.content}')
            
    def get_skills(self, ngramma):
        result = []
        for node in self.nodes:
            if node.key == ngramma:
                result += node.content
        return result
    
    def get_skills_dictionary(self):
        return {node.key: node.content for node in self.nodes}




class Node:
    def __init__(self, name, number, withs = [], out = True):
        self.key = ' '.join(list(Stem_text(name)))
        self.name = name
        self.number = number
        self.withs = withs
        self.out = out
        






if __name__ == '__main__':
    g = Graph('graph_skills.txt')
    
    g.print()

    print()
    g.print_content()
    
    dr = os.path.dirname(__file__)
    _to = os.path.join(dr, 'graph_skills.json')
    
    with io.open(_to,'w', encoding = 'utf-8') as f:
        json.dump(g.get_skills_dictionary(), f, indent=4)
    








