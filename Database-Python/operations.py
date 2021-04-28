import os 
import sqlOps as sql 
from os import system 
from user import User

system('clear')

#func.readUserInfo()
users = []
def readUserOperation():
    func.readUserInfo()

def insertOperation():
    numberOfEntries = int(input('Enter number of records >> '))
    for entry in range(numberOfEntries):
        print(f'--- User # {entry + 1} ---')
        user = User()
        fname = input('What is your first name? >> ')
        user.setFirstName(fname)
        lname = input('What is your last name? >> ')
        user.setLastName(lname)
        age = int(input('What is your age? >> '))
        user.setAge(age)
        phone = input('What is your phone? >> ')
        user.setPhone(phone)
        users.append(user)
        print()
    for user in users:
        sql.insertUserInfo(user.getFirstName(), user.getLastName(), user.getAge(), user.getPhone())

def updateOperation():
    print()

def deleteOperation():
    sql.readUserInfo()
    userId = int(input('which id do you want to delele? >> '))
    sql.deleteUser(userId)
