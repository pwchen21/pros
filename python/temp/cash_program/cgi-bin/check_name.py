#! /usr/local/bin/python3

import sqlite3
import cgi
import yate

form=cgi.FieldStorage()
name=form["UserName"].value
inpw=form["Password"].value
"""補使用者名稱不存在"""

connection = sqlite3.connect('money.sqlite')
cursor = connection.cursor()

cursor.execute('SELECT pw FROM account WHERE name=?', [name])
pw=cursor.fetchone()[0]
connection.commit()
connection.close()

if inpw == pw:
    print("OK")
    print(yate.start_response())
    print(yate.include_header("auth OK"))
    print(yate.include_footer({"Home": "/index.html"}))

else:
    print("fail")
    print(yate.start_response())
    print(yate.include_header("auth fail"))
    print(yate.include_footer({"Home": "/index.html"}))
