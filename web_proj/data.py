import sqlite3 as db 
conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("drop table if exists temps")
cursor.execute("create table temps(date test, temp int)")
cursor.execute('insert into temps values("12/1/2014", 35)')
cursor.execute('insert into temps values("12/2/2014", 42)')
cursor.execute('insert into temps values("12/3/2014", 41)')
cursor.execute('insert into temps values("12/4/2014", 40)')
cursor.execute('insert into temps values("12/5/2014", 23)')
conn.row_factory = db.Row
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
	print ("%s %s" % (row[0], row[1]))
cursor.execute("select avg(temp) from temps")
row = cursor.fetchone()
print("The avarage was %s"% row)
