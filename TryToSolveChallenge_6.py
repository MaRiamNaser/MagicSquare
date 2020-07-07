# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:54:12 2020

@author:  Moaaz Hasan
          Mariam Nasser
"""


import math as mt
import numpy



def challenge6():
    print('Start')
    # flag = True
    i = 9
    while(i < 1000):
        for j in range(1,1000):
            for k in range(j+1,1000):
                #print('i:',i)
                #print('j:',j)
                #print('K:',k)
                Sum = i**2 + j**2 + k**2
                if(mt.sqrt(Sum) % 2 != 0) and Sum % 3 == 0:
                    Center = Sum // 3
                    if(mt.sqrt(Center) % 2 == 0):
                        list = [i**2,j**2,k**2,Center]
                        x3 = Sum - (Center + k**2)
                        if x3 > 0:
                            if ((i**2 + j**2 + k**2) == Sum):
                                if(x3 not in list):
                                    if(mt.sqrt(x3) % 2 == 0):
                                        list.append(x3)
                                        x6 = Sum -(x3 + i**2)
                                        if x6 > 0:
                                            if(x6 not in list):
                                                if(mt.sqrt(x6) % 2 == 0):
                                                    list.append(x6)
                                                    x4 = Sum - (Center + x6)
                                                    if x4 > 0:
                                                        if(x4 not in list):
                                                            if(mt.sqrt(x4) % 2 == 0):
                                                                list.append(x4)
                                                                x2 = Sum - (j**2 + Center)
                                                                if x2 > 0:
                                                                    if(x2 not in list):
                                                                        if(mt.sqrt(x2) % 2 == 0):
                                                                            list.append(x2)
                                                                            x1 = Sum - (k**2 + x4)
                                                                            if x1 > 0:
                                                                                if(x1 not in list):
                                                                                    if(mt.sqrt(x1) % 2 == 0):
                                                                                        list.append(x1)
                                                                                        print('res','i:',i**2,'j:',j**2,'K:',k**2,'Center',Center,'Sum:',Sum,'x3:',x3,'x6:',x6 ,'x4:',x4,'x2:',x2,'X1:',x1)
                                                                                        print(list)
                    list = []

                        #flag = False
                        #break
                #if(not flag):
                    #break
        i += 1
    print('End')
