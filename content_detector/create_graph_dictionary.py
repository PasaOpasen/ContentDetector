# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:37:43 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname(__file__))
from stemmer_rus import Stem_text
import json



class Graph:
    def __init__(self, filename):
        with io.open(filename, 'r', encoding = 'utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
        lines = filter(lambda line: len(line) > 0 and not line.startswith('#'), lines)
        
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
            
        print()
        skills = [node.name for node in self.nodes if node.out]
        print(f'total nodes: {len(self.nodes)}')
        print(f'total skills = {len(skills)}: {skills}')
            
    def get_skills(self, ngramma):
        result = []
        for node in self.nodes:
            if node.key == ngramma:
                result += node.content
        return result
    
    def get_skills_dictionary(self):
        return {node.key: node.content for node in self.nodes}
    
    def rewrite_graph(self, from_file, to_file):
        """
        перезаписывает файл графа так, чтоб корни определялись до первого использования
        это нужно затем, чтоб не случалось переопределений хотя бы самых основных навыков
        """
        
        names = [node.name for node in self.nodes if len(node.withs) == 0]
        
        with io.open(from_file, 'r', encoding = 'utf-8') as f:
            lines = [line for line in f.readlines()]
        
        for name in names:
            
            definition = position = len(lines)
            
            for i, line in enumerate(lines):
                s = line.strip()
                if len(s)>0:
                    path = s.split('|')
                    words = path[0].split(',')
                    if len(path)>1:
                        words+=path[1].split(',')
                    
                    words = [word.strip() for word in words]
                    #print(words)
                    
                    if len(words)==1 and words[0] == name:
                        definition = i
                    elif name in words and position == len(lines):
                        position = i
            
            if position < definition:
                print(f'position of first using of {name}({position}) is upper than definition ({definition if definition < len(lines) else "no definition"})')
                lines.insert(position, name+'\n')
            
        
            
        with io.open(to_file, 'w', encoding = 'utf-8') as f:
            f.writelines([line+'\n' for line in lines])
        
    
    def show_graph_pdf(self):
        from graphviz import Digraph
        dot = Digraph(filename='gpaph.gv', 
                      #engine='sfdp'
                      #engine='neato'
                      engine='fdp'
                      )
        #dot.attr(size='6,6')
        
        for node in g.nodes:
            
            if node.out:
                dot.attr('node', shape='box')
            else:
                dot.attr('node', shape='circle')
            
            dot.node(f'{node.number}', node.name)
        for node in g.nodes:
            for n in node.withs:
                dot.edge(f'{node.number}', f'{n}', constraint='true')
        dot.view()
        
    @staticmethod    
    def update_graph():
        dr = os.path.dirname(__file__)
        g = Graph(os.path.join(dr,'graph_skills.txt'))
        
        print()
        g.print_content()
           
        _to = os.path.join(dr, 'graph_skills.json')
        
        #with io.open(_to,'w', encoding = 'utf-8') as f:
        #with open(_to,'w', encoding = 'utf-8') as f:
        with open(_to,'w', encoding = 'utf-8') as f:
            json.dump(g.get_skills_dictionary(), f, indent=4)
            
        with open(os.path.join(dr, 'supported_skills.txt'), 'w', encoding = 'utf-8') as f:
            t = sorted((node.name for node in g.nodes if node.out))
            f.writelines('\n'.join(t))


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
    
    #with io.open(_to,'w', encoding = 'utf-8') as f:
    #with open(_to,'w', encoding = 'utf-8') as f:
    with open(_to,'w', encoding = 'utf-8') as f:
        json.dump(g.get_skills_dictionary(), f, indent=4)
        
        
    g.show_graph_pdf()
    
    #g.rewrite_graph('graph_skills.txt','graph2_skills.txt')
    








