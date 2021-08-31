from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ open")
	cursor=con.cursor()
	sql="select * from student"
	cursor.execute(sql)
	data=cursor.fetchall()
	print(data)                         #list of tuples  [(rno,name,marks),(...),()]

	for d in data:
		print("rno=",d[0],'name=',d[1],'marks=',d[2])

except Exception as e:
	print("Issue",e)
finally:
	if con is not None:
		con.close()
		print("Closed")