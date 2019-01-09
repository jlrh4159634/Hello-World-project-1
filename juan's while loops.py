'''
1) Swap two variables
2)Fibonacci sequence
'''

# a=5
# b=10
# print ('the value for a=',a,'and the value for b = ',b)
#
# #create a temporary variable which is named temp
#
# temp=a #place the value from a into temp
# a=b #assign to var a the content of b
# b= temp #assign b the temp value
#
# print ('the value for a=',a,'and the value for b = ',b)
#
#
#
# #WHILE LOOPS
#
# x=1
# while x<10:
#     print (x)
#     x=x+1
#
# cont= 'c'
# while cont =='c':
#     print("press c if u want more, otherwise press any key")
#
#     cont=input('enter c if want more')
#

x=1
y=1
cont='c'
while cont=='c':
    print ('A new Fibon number is' , x+y)
    temp= x
    x=y
    y=y + temp
    cont=input('if u want more Finon numbers press c, else press any!')