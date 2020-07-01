# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:47:30 2020

@author: qtckp

https://www.geeksforgeeks.org/performing-google-search-using-python-code/

https://github.com/aviaryan/python-gsearch
"""



try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "майкрософт офис"

query = 'на английском'
  
for j in search(query, tld="co.in", lang='en',  num=10, stop=10, pause=2): 
    print(j) 








