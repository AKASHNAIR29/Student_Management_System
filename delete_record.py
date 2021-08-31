from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ opened")
	cursor=con.cursor()
	sql="delete from student where rno='%d'" 
	rno=int(input("enter rno to be deleted "))
	cursor.execute(sql % (rno))
	if cursor.rowcount>0:
		print("record deleted")
		con.commit()
	else:
		print('record doesnt exist')

except Exception as e:
	print("Issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("Closed")