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


def challengeFour(inp1, inp2 ):

    flag = True
    c = 1

    FinalMagicSqure = [0,0,0,0,0,inp1,0,inp2,0]
    x11 = (inp1+inp2)/2
    FinalMagicSqure[0] = int(x11)


    while(flag):

        magicSqure = FinalMagicSqure[:]
        x22 = magicSqure[0] + c
        x99 = magicSqure[7] + c

        if x22 in magicSqure:
            c += 1
            continue
        if x99 in magicSqure:
            c += 1
            continue

        if not ( ( ( (magicSqure[0] + x99) / 2) ==  ((x22 + magicSqure[7]) / 2) ) and ( (magicSqure[0] + x99) % 2 == 0 )) :
            c += 1
            continue
        magicSqure[1] = int(x22)
        magicSqure[8] = int(x99)
        magicSqure[4] = int((magicSqure[0] + magicSqure[8]) / 2)
        magicSum = int(magicSqure[1] + magicSqure[4] + magicSqure[7])
        x33 = magicSum - (magicSqure[5] + magicSqure[8])

        if (x33 in magicSqure) :
            c += 1
            continue

        magicSqure[2] = int(x33)
        x77 = magicSum - (magicSqure[7] + magicSqure[8])

        if (x77 in magicSqure) :
            c += 1
            continue
        magicSqure[6] = int(x77)
        x44 = magicSum - (magicSqure[0] + magicSqure[6])

        if (x44 in magicSqure) :
            print(x44,'Bawaztani')
            c += 1
            continue
        magicSqure[3] = int(x44)

        FinalMagicSqure = magicSqure[:]
        flag = False

    print('---------------------------')
    print('Challenge 4')
    c = 0
    for i in range(3):
        for j in range(3):
            print(FinalMagicSqure[c] ,end='   ')
            c +=1
        print('')
    print('Magic Sum is :',magicSum)


def challengeFive(inp1, inp2 ):

    flag = True
    c = 1
    smallest = 1
    magicSums = []
    FinalMagicSqure = [0,0,0,0,0,inp1,0,inp2,0]
    x11 = (inp1+inp2)/2
    FinalMagicSqure[0] = int(x11)
    arrayFinalMagicSqure = []

    while(flag):
        magicSqure = FinalMagicSqure[:]
        x22 = magicSqure[0] + c
        x99 = magicSqure[7] + c

        if x22 in magicSqure:
            c += 1
            continue
        if x99 in magicSqure:
            c += 1
            continue

        if not ( ( ( (magicSqure[0] + x99) / 2) ==  ((x22 + magicSqure[7]) / 2) ) and ( (magicSqure[0] + x99) % 2 == 0 )) :
            c += 1
            continue
        magicSqure[1] = int(x22)
        magicSqure[8] = int(x99)
        magicSqure[4] = int((magicSqure[0] + magicSqure[8]) / 2)
        magicSum = int(magicSqure[1] + magicSqure[4] + magicSqure[7])
        x33 = magicSum - (magicSqure[5] + magicSqure[8])
        if (x33 in magicSqure) :
            c += 1
            continue

        magicSqure[2] = int(x33)
        x77 = magicSum - (magicSqure[7] + magicSqure[8])
        if (x77 in magicSqure) :
            c += 1
            continue
        magicSqure[6] = int(x77)
        x44 = magicSum - (magicSqure[0] + magicSqure[6])

        if (x44 in magicSqure) :
            c += 1
            continue
        magicSqure[3] = int(x44)

        arrayFinalMagicSqure.append(magicSqure[:])
        magicSums.append(magicSum)
        smallest +=1
        c +=1
        if smallest == 4:
            flag = False

    print('---------------------------')
    print('Challenge 5')
    m = 0
    for i in arrayFinalMagicSqure:
        print('******** Smallest (',m + 1,') ********')
        c = 0 ;
        for k in range(3):
            for j in range(3):
                print(i[c] ,end='   ')
                c +=1
            print('')
        print('Magic Sum is:', magicSums[m]) ; m += 1





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
    challengeFour(18,28) # Positions at x6 and x8
    challengeFive(18,28)  # Positions at x6 and x8 _ The First three smallest magic sum.
   

if __name__ == "__main__": main()







