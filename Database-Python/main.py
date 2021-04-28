import os  
from os import system 
import operations as ops


system('clear')

operationsList = ['Read', 'Insert', 'Update', 'Delete']

counter = 1

print('These are the opeations that you can perform in our database: ')
for operation in operationsList:
    print(f'{counter}. {operation}')
    counter += 1
choice = int(input('Select one above >> '))

if (choice == 1):
    ops.readUserOperation()
elif (choice == 2):
    ops.insertOperation()
elif (choice == 4):
    ops.deleteOperation()
else:
    print('invalid selection')

