'''
Documentation
=o;lll[
'''

import random

secret = random.randint(1,99)

guess = 0
tries = 0
print ("Can you guess my number?")
print ("My number is an integer between 1 and 99")


while guess != secret and tries  < 6:
    print ("What is your guess")
    guess = int (input())
    if guess < secret :
        print ("Too low!")
    elif guess > secret :
        print ("Too high")
    tries = tries + 1


if guess == secret :
    print ("You got it! Well done!")
else :
    print ("No more guesses! Try again")
    print ("The secret number was:" , secret)