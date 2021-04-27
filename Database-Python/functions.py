import connection as c 
import mysql.connector

def readUserInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        for row in cursor:
            print(f'''
            id .............. {row[0]}  
            First Name ...... {row[1]}   
            Last Name ....... {row[2]}
            Age.............. {row[3]}
            Phone ........... {row[4]}        
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)