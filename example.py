# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:32:45 2020

@author: qtckp
"""

import os

from content_detector.detector import get_content_from_text



if __name__=='__main__':
    
    
    lines = [
        "знаю JS, CSS, C++",
             'ms word, excel']
    print(get_content_from_text(lines))
    
    
    for file_number in (0,1,2,3,4,5):
        
        print()
        with open(f"{os.path.dirname(__file__)}/learning/train_samples/{file_number}.txt", 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
        
        answer = get_content_from_text(lines)
        print(f"file {file_number}:")
        print(answer)


