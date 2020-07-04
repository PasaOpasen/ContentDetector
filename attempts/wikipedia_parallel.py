# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 02:43:09 2020

@author: qtckp
"""

import os
import wikipedia
from multiprocessing import Pool
import time
import multiprocessing

# без этой обёртки не будет работать
def pickle_search(text):
    return wikipedia.search(text)

def wiki_search(text, dictionary):
    t = wikipedia.search(text)
    dictionary[text] = t
    print(t)

pool = Pool(os.cpu_count())


%time r1 = [wikipedia.search(f's{i}') for i in range(30)] # 36 secs

# не прекращается
%time r2 = pool.map(pickle_search, [f'p{i}' for i in range(30)]) # don't stop working



# работает секунду, но нет результатов (кэш у функции тоже пустой)
starttime = time.time()
processes = []
manager = multiprocessing.Manager()
return_dict = manager.dict()

for i in range(0,30):
    p = multiprocessing.Process(target=wiki_search, args=(f'q{i}',return_dict))
    processes.append(p)
    p.start()
        
for process in processes:
    process.join()
        
print('That took {} seconds'.format(time.time() - starttime))
print(return_dict)





# не прекращается

def foo_pool(x):
    return wikipedia.search(x)

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list+=result



pool = Pool()
for i in range(30):
    pool.apply_async(foo_pool, args = (f'p{i}' , ), callback = log_result)
pool.close()
pool.join()
print(result_list)
    
























