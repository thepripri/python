import json, os
from os import system
from json import load, dumps

system('clear')

with open('./Modules-and-Libraries/users.json', 'r') as file:
    datastore = load(file)
print(datastore)
# for data in datastore:
#     print(f'''
#     ---------------------------------
#     Hello, {data['name']}
#     This is the information we have about you:
#     Name: {data['name']}
#     Age: {data['age']}
#     Educational Level: {data['Educational_Level']}
#     SSN: {data['SSN']}
#     ''')