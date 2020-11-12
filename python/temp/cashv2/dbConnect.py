import sqlite3

conn = sqlite3.connect(<DB Name>)
# open connection 
c=conn.cursor()
#create cursor object before execute sql command
c.execute('''<sql command>''')
# execute sql command
conn.commit()
conn.close()
