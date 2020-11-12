#! /usr/local/bin/python3

import sqlite3
connection = sqlite3.connect('money.sqlite')

cursor = connection.cursor()
cursor.execute("""CREATE TABLE account (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    pw TEXT NOT NULL )""")
cursor.execute("""INSERT INTO account(name, pw) VALUES('admin', 'admin')""")

connection.commit()
connection.close()
