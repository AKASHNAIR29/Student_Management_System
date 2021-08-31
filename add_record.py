from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ opened")
	cursor=con.cursor()
	sql="insert into student values('%d','%s','%d')"
	rno=int(input("enter rno "))
	name=input("enter name ")
	marks=int(input("enter marks "))	
	cursor.execute(sql % (rno,name,marks))
	print("record added")
	con.commit()

except Exception as e:
	print("Issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("Closed")