# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 06:32:19 2020

@author: ELCOT
"""

import numpy as np

x = list("385461279296375841741289365417592638862713954539648127124956783658137492973824516")
y = list("111101011100101011001110110110111101010111010101111011011011100110101001110101111")

for i in range(len(x)):
    if y[i] == '1':
        x[i] = '.'


ret = []
cnt = 0

tmp = []
for i in range(len(x)):
    if (cnt >= 9):
        ret.append(tmp)
        cnt = 0
        tmp = []
    tmp.append(x[i])
    cnt += 1
ret.append(tmp)
    
print(ret)
        
