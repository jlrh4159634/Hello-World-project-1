'''
Find the number of digits in a given number
'''

num=int(input("enter your number :")) #enter a positive integer using the keyboard
dig=1 #start with the 1 as a power of ten (dig=1)

while num>10** dig: #evaluate the condition number less than 10 to the power of dig
    dig=dig+1 #if condition true execute the loop body
               #increase dig by one number

print(num, "has", dig, "digits")  #if condition false exit loop and print the results
