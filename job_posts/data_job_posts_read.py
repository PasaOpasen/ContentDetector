# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:30:25 2020

@author: qtckp
"""


import pandas as pd


data = pd.read_csv('data job posts.csv') 

print(data.columns)

data = data.iloc[:,[12,13]]


j1 = data.iloc[:,0].dropna().values

j2 = data.iloc[:,1].dropna().values


with open('JobReqirments.txt','w') as f:
    for p in j1:
        f.writelines(p)


with open('RequiredQual.txt','w') as f:
    for p in j2:
        f.writelines(p)
