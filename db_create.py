from sqlite3 import *

con = None
try:
	con = connect("akashproject.db")
	print("Database created/ open")
except Exception as e:
	print("Issue",e)
finally:
	if con is not None:
		con.close()
		print("Closed")