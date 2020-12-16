'''
Integrate SQL with Python by importing the MySQL module
'''
import mysql.connector as sqltor
from mysql.connector import Error

connection = sqltor.connect(host='localhost', database='Haziq', user='root', password='c9070baa')
try:
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
