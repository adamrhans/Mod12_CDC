from lib2to3.refactor import MultiprocessRefactoringTool
import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='M@v3r!ck',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `media`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS media")
cursor.execute(query)

# use db
query = ("USE media")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE movies(
    title VARCHAR(30),
    release_date VARCHAR(50),
    rating VARCHAR(10)
);
''')

cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    

