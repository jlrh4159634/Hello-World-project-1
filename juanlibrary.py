'''
put here all the definitions for specific formulas
'''
import math

def fibon_sequence(n):
    x = 1
    y = 1
    cont = 1
    while cont <= n:
        print('A new Fibon number is', x + y)
        temp = x
        x = y
        y = y + temp
        cont = cont +1

fibon_sequence(20)
