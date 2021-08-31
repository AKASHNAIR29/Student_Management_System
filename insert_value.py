from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ open")
	cursor=con.cursor()
	sql="insert into student values(22,'zaddy',99)"   #ekhi sql stmt hota at a time
	cursor.execute(sql)
	print("record created")
	con.commit()
except Exception as e:
	print("Issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("Closed")