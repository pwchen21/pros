#! /usr/local/bin/python3

import sqlite3

name="admin"

connection = sqlite3.connect('test.sqlite')
cursor = connection.cursor()
cursor.execute("""SELECT pw FROM account WHERE name="admin"; """)
pw=cursor.fetchone()[0]
connection.commit()
connection.close()

print(pw)
