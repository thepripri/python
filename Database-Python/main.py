import os 
import functions as func 
from os import system 


system('clear')

#func.readUserInfo()

fname = input('What is your first name? >> ')
lname = input('What is your last name? >> ')
age = int(input('What is your age? >> '))
phone = input('What is your phone? >> ')

func.insertUserInfo(fname, lname, age, phone)


