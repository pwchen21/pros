import sqlite3

conn=sqlite3.connect(r'D:\se\py\db\test.db')

# Create Table
#conn.execute('CREATE TABLE USER ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, `NAME` TEXT NOT NULL, `NICKNAME` TEXT, `PASSWORD` TEXT, `MAIL` TEXT )')

# Insert Data

'''
conn.execute('INSERT INTO USER (NAME, NICKNAME) VALUES ("Tester1", "N1");')
conn.execute('INSERT INTO USER (NAME, NICKNAME) VALUES ("Tester2", "N2");')
conn.execute('INSERT INTO USER (NAME, NICKNAME) VALUES ("Tester2", "N2");')
'''

# Commit Insert
conn.commit()

# Get User Data
cursor=conn.execute('SELECT P from USER')

# Print Data in ROW
for x in cursor:
	#print('ID: ', x[0],' ','NAME:', x[1],' ', 'NICKNAME: ', x[2])
	if x[1] == 'Tester1':
		print('Nickname:', x[2])

conn.close()


		#, (idr.get(), nic.get(), mailr.get(), pwr.get()))