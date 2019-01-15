'''
put here all the definitions for specific formulas
'''
import math

# def fibon_sequence(n):
#     x = 1
#     y = 1
#     cont = 1
#     while cont <= n:
#         print('A new Fibon number is', x + y)
#         temp = x
#         x = y
#         y = y + temp
#         cont = cont +1
#
# fibon_sequence(20)




def distance2d (x1, y1, x2, y2):
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return d

def distance3d (x1, y1, z1, x2, y2,z2 ):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2+(z1-z2)**2)
    return d

