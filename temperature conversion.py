'''
Convert from F to C, and from C to F
'''

degree = input("enter lower case c for celsius, and f for farenheit:")
temp=int(input("enter the temperature's value:"))

if degree =='f':
    C=(temp-32)*5/9
    print ("the conversion in celsius is : ",round (C))
elif degree == 'c':
    f=temp*9/5+32
    print("the conversion in Farenheit is :",round (F))


else:
   print("there si not such type of temperature:", degree)

