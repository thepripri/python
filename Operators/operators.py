import os, math, time
from os import system
from colorama import Fore, Style
from math import pow, floor, ceil
from time import sleep
system('clear')


# exponentiation => 3 elevated to the power of 2 => operator **
print('Exponentiation using 3 ** 2 = ', 3 ** 2) 
# math pow() to elevate first argument to the second one
print('Exponentiation using pow(3, 2) = ', pow(3, 2))

print('floor of 10//3 = ', 10//3) # returns the floor of 10/3, equivalent to line 14
print('floor of floor(10/3) = ', floor(10/3)) # returns the floor of 10/3, equivalent to line 13

x = 10/4
flr = floor(x)
cl = ceil(x)

print(f'Floor of {x} is {flr}, Ceil of {x} is {cl}')

liters = 12.5
gallons = 12.5 / 3.7

print('''
    How many gallons do I need?
    Well, after careful consideration and having {liters} liters. I have come to 
    realize that I need:''')

print()
print(Fore.MAGENTA, 'THINKING NOW...')
sleep(4)
print(f'approximately {ceil(gallons)} gallons')


# # Check this page out for more on operators
# https://docs.python.org/3.9/library/operator.html

system('clear')
print()
print()
def calculate(a1):
    print(a1)

def calculate(a1, a2 = None):
    print(a1, a2)

def calculate(a1, a2 = None, a3 = None):
    print(a1, a2, a3)

def calculate(a1, a2 = None, a3 = None, a4 = None):
    print(a1, a2, a3, a4)


calculate(1, 2, 3, 4)