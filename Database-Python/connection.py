import mysql.connector, os
from os import environ
from mysql.connector import connect 

def returnConnection():
    conn = connect(
        host = 'mydatabase.cfrbdcbviyqw.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'pass1976',
        database = 'myDB'
    )
    return conn

returnConnection()