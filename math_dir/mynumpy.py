#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:19:10 2018

@author: crupib
"""

import numpy as np


my_array = np.ones((3,4))

#print(my_array)

empty_array = np.zeros((3,4))

#print(empty_array)

my_random = np.random.rand(3,4)

#print(my_random)

wines = np.genfromtxt('wines.csv')

#print(wines)
#print('--------------------------------------------------------------------')
third_wine = wines[3,:]
#print(third_wine)
#print('--------------------------------------------------------------------')
newwines = wines.astype(int)
sum = 0
for j in range(0,4):
        for x in newwines[j] :
#           sum += x
            print ('x= '+ str(x))  
#        print('--------------------------------------------------------------------')
#        print(sum)