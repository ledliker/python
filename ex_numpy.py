# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:09:48 2021

@author: lasttrain
"""

import numpy as np

a = np.array([1,2,3])
a1 = np.array([[1,2,3]])
a2 = np.array([
    [1,2,3],
    [1,2,3]
    ])
a3 = a2[:, 1:]

b = np.array([1,2,3])

# print(a)
# print(a.T)
# print(a1)
# print(a1.T)
# print(a2)
# print(a2.T)
# print(a3)
# print(a3.T)

# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))
# print(np.dot(a2,a2.T))
# print(np.dot(a1,a))

sum_ab(a, b)

