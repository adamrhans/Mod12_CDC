import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='M@v3r!ck',
    host='127.0.0.1',
    database='media',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

sql = (f'INSERT INTO movies VALUES (%s,%s,%s)')

values = [
    ("Pacific Rim", "2013-07-12", "PG-13"),
    ("Godzilla vs. Kong","2021-03-05","PG-13"),
    ("Rogue One: A Star Wars Story","2016-12-14","PG-13"),
]

cursor.executemany(sql,values)

# clean up
cnx.commit()
cursor.close()
cnx.close()    