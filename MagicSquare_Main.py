# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:54:12 2020

@author:  Moaaz Hasan
          Mariam Nasser
"""

import sympy as sym

sym.init_printing()


def challengeOne(inp1, inp2 , inp3 , inp4):
    res = []
    x1,x2,x3,x4,x5,x6,x7,x8,x9,n = sym.symbols(str(inp1) +','+ str(inp2) +','+ str(inp3) +','+ str(inp4) +','+ 'x5,x6,x7,x8,x9,n')

    f1 = sym.Eq(x1+x2+x3,n)
    f9 = sym.Eq((x1+x9)/2,x5)
    f14 = sym.Eq((x4+x2)/2,x9)
    f15 = sym.Eq(n - (x1+x4),x7)
    f17 = sym.Eq((x2+x6)/2,x7)
    f23 = sym.Eq(x1+x2+x3+x5+x7+x9+x4+x8+x6,3*n)

    res = sym.solve( [f1,f9,f14,f15,f17,f23] ,(x5,x6,x7,x8,x9,n) )

    list = [sym.expand(str(v)) for k,v  in res.items()]
    finalMagicSqure =  [inp1,inp2,inp3,inp4]
    finalMagicSqure.extend(list)
    print('---------------------------')
    print('Challenge 1')
    c = 0
    for i in range(3):
        for j in range(3):
            print(finalMagicSqure[c] , '  ',end='')
            c +=1
        print('')
    print('Magic Sum is :',finalMagicSqure[-1])


def challengeTwo(inp1, inp2 , inp3 , inp4):
    finalMagicSqure = []

    x1,x2,x3,x4,x5,x6,x7,x8,x9,n = sym.symbols('x1,' + str(inp1) +','+ str(inp2) +','+ str(inp3) +','+  'x5,x6,x7,x8,' + str(inp4) +',n')

    f1 = sym.Eq(x3+x6+x9,n)
    f2 = sym.Eq((x1+x9)/2,x5)
    f3 = sym.Eq(n/3,x5)
    f4 = sym.Eq(n-(x1+x4),x7)
    f5 = sym.Eq((x2+x6)/2,x7)
    f6 = sym.Eq(x1+x2+x3+x5+x7+x9+x4+x8+x6,3*n)

    res = sym.solve( [f1,f2,f3,f4,f5,f6] ,(x1,x5,x6,x7,x8,n) )

    list = [sym.expand(str(v)) for k,v  in res.items()]
    finalMagicSqure = list[:]
    finalMagicSqure.insert(1,inp1)
    finalMagicSqure.insert(2,inp2)
    finalMagicSqure.insert(3,inp3)
    finalMagicSqure.insert(8,inp4)

    print('---------------------------')
    print('Challenge 2')
    c = 0
    for i in range(3):
        for j in range(3):
            print(finalMagicSqure[c] , '    ',end='')
            c +=1
        print('')

    print('Magic Sum is :',finalMagicSqure[-1])


def challengeThree(inp1, inp2 , inp3):

    x1,x2,x3,x4,x5,x6,x7,x8,x9,n = sym.symbols('x1,x2,x3,' + str(inp1) +','+'x5,'+ str(inp2) +',x7,'+  str(inp3) + ',x9,n')

    f1 = sym.Eq(3*x5,n)
    f2 = sym.Eq(n - (x5 + x8) , x2)
    f3 = sym.Eq((x8+x6)/2,x1)
    f4 = sym.Eq((x4+x2)/2,x9)
    f5 = sym.Eq((x4+x8)/2,x3)
    f6 = sym.Eq((x2+x6)/2,x7)
    f7 = sym.Eq((x4+x6)/2,x5)

    res = sym.solve( [f1,f2,f3,f4,f5,f6,f7] ,(x1,x2,x3,x5,x7,x9,n) )

    list = [sym.expand(str(v)) for k,v  in res.items()]
    finalMagicSqure = list[:]
    finalMagicSqure.insert(3,inp1)
    finalMagicSqure.insert(5,inp2)
    finalMagicSqure.insert(7,inp3)

    print('---------------------------')
    print('Challenge 3')
    c = 0
    for i in range(3):
        for j in range(3):
            print(finalMagicSqure[c] ,end='   ')
            c +=1
        print('')
    print('Magic Sum is :',finalMagicSqure[-1])



def main():

    # We use equations to solve challenge 1 ,2 and 3 by sympy library

    # Matrix Positions:
    # x1  x2  x3
    # x4  x5  x6
    # x7  x8  x9

    print('Welcome to Magic Square Challenges by: Moaaz Hasan and Mariam Nasser .')
    challengeOne(2,7,6,9) # Positions at x1, x2 ,x3 and x4
    challengeTwo(7,16,15,11) # Positions at x2, x3 ,x4 and x9
    challengeThree(31,15,41) # Positions at x4, x6 ,x8
   

if __name__ == "__main__": main()







