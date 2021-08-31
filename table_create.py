from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ open")
	cursor=con.cursor()
	sql="create table student(rno int primary key,name text,marks int)"
	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("Issue",e)
finally:
	if con is not None:
		con.close()
		print("Closed")