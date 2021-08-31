from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4

#validation ke liye

def validate(rv, nv, mv):
	r = rv; n = nv; m = mv;
	#print(r,n,m)
	if r == "":
		showerror('Error', 'Rno cannot be blank.')
		add_window_ent_rno.delete(0,END)
		update_window_ent_rno.delete(0,END)
		add_window_ent_rno.focus()
		update_window_ent_rno.focus()
		return(None,None,None)
	elif not r.isdigit():
		showerror('Error','Roll has to be numeric.')
		add_window_ent_rno.delete(0,END)
		update_window_ent_rno.delete(0,END)
		add_window_ent_rno.focus()
		update_window_ent_rno.focus()
		return(None,None,None)
	elif int(r) == 0:
		showerror('Error', 'Rno cannot be zero.')
		add_window_ent_rno.focus()
		update_window_ent_rno.focus()
		return(None,None,None)
	elif int(r) < 0:
		showerror('Error', 'Rno should be positive integers.')
		add_window_ent_rno.focus()
		update_window_ent_rno.focus()
		return(None,None,None)
	elif n == "":
		showerror('Error', 'Name cannot be blank.')
		add_window_ent_name.focus()
		update_window_ent_name.focus()
		return(None,None,None)
	elif not n.isalpha():
		showerror('Error', 'Name cannot be numeric')
		add_window_ent_rno.delete(0,END)
		update_window_ent_rno.delete(0,END)
		add_window_ent_name.focus()
		update_window_ent_name.focus()
		return(None,None,None)
	elif (len(n)) < 2:
		showerror('Error', 'Please enter a valid name.')
		add_window_ent_name.focus()
		update_window_ent_name.focus()
		return(None,None,None)
	elif m == "":
		showerror('Error', 'Marks cannot be blank.')
		add_window_ent_marks.focus()
		update_window_ent_marks.focus()
		return(None,None,None)
	elif not m.isdigit():
		showerror('Error','Marks has to be numeric.')
		add_window_ent_marks.delete(0,END)
		update_window_ent_marks.delete(0,END)
		add_window_ent_marks.focus()
		update_window_ent_marks.focus()
		return(None,None,None)
	elif int(m) < 0 or int(m) > 100: 
		showerror('Error', 'Marks should be in range 0-100.')
		add_window_ent_rno.delete(0,END)
		update_window_ent_rno.delete(0,END)
		add_window_ent_marks.focus()
		update_window_ent_marks.focus()
		return(None,None,None)

	else:
		vrno = int(r); vname = n; vmarks = int(m)
		return(vrno, vname, vmarks)


#add button ke liye

def f1():
	add_window.deiconify()      #add open main close(main ka add button dabaya tho)
	main_window.withdraw()   
	add_window_ent_rno.focus()   
	main_window.configure(background='black')
	main_window_btn_add.configure(background='red')

def f2():
	main_window.deiconify()      #add close main open(back btn add ke andar wala dabaya tho)
	add_window.withdraw()

def f3():                                                #(save btn add ke andar wala dabaya tho)
	con = None
	rno = add_window_ent_rno.get()
	name = add_window_ent_name.get()
	marks = add_window_ent_marks.get()
	vrno, vname, vmarks = validate(rno, name, marks)
	if vrno != None:
		try:
			con = connect('akashproject.db')
			cursor = con.cursor()
			sql = "insert into student values('%d', '%s','%d')"
		
			rno = int(add_window_ent_rno.get())
			name = add_window_ent_name.get()
			marks = int(add_window_ent_marks.get())
			cursor.execute(sql % (rno, name,marks))
			con.commit()
			showinfo('Success', 'Record added')
	


			add_window_ent_rno.delete(0,END)
			add_window_ent_name.delete(0,END)
			add_window_ent_marks.delete(0,END)
		except Exception as e:
			showerror('Failure', e)
		finally:
			if con is not None:
				con.close()

			

#view button ke liye


def f4():                                 #view close main open(back btn view ke andar wala dabaya tho)
	main_window.deiconify()
	view_window.withdraw()

def f5():                                  #view open main close(main ka view button dabaya tho)
	view_window.deiconify()
	main_window.withdraw()
	main_window.configure(background='black')
	main_window_btn_view.configure(background='lime')
	view_window_st_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect('akashproject.db')
		cursor = con.cursor()
		sql = "select * from student order by rno"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " Roll No. = " + str(d[0]) +  "   Name = " + str(d[1]) +  "    Marks = " + str(d[2]) +     "\n"
		view_window_st_data.insert(INSERT, info)

	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()




		


#update button ke liye

def f6():
	update_window.deiconify()      #update open main close(main ka update button dabaya tho)
	main_window.withdraw()    
	main_window.configure(background='black')
	main_window_btn_update.configure(background='pink') 

def f7():
	main_window.deiconify()      #update close main open(back btn update ke andar wala dabaya tho)
	update_window.withdraw()

def f8():                                     #(save btn update ke andar wala dabaya tho)
	con = None
	rno = update_window_ent_rno.get()
	name = update_window_ent_name.get()
	marks = update_window_ent_marks.get()
	vrno, vname, vmarks = validate(rno, name, marks)
	if vrno != None:
		try:
			con = connect("akashproject.db")
			cursor=con.cursor()
			sql="update student set name='%s',marks='%d' where rno='%d'" 
	
			cursor.execute(sql % (vname,vmarks,vrno))
			if cursor.rowcount>0:
				showinfo('Success', 'Record updated')
				con.commit()
			else:
				showerror('Retry', 'Record doesnt exist')

			update_window_ent_rno.delete(0,END)
			update_window_ent_name.delete(0,END)
			update_window_ent_marks.delete(0,END)

		except Exception as e:
			showerror('Failure', e)
			con.rollback()
		finally:
			if con is not None:
				con.close()



#delete button ke liye

def f9():
	delete_window.deiconify()      #delete open main close(main ka delete button dabaya tho)
	main_window.withdraw()      
	main_window.configure(background='black')
	main_window_btn_delete.configure(background='cyan')

def f10():
	main_window.deiconify()      #delete close main open(back btn delete ke andar wala dabaya tho)
	delete_window.withdraw()


def f11():                                                #(save btn delete ke andar wala dabaya tho)
	con = None
	rno = delete_window_ent_rno.get()
	if rno=='':
		showwarning("Warning","Roll cannot be blank.")
		delete_window_ent_rno.focus()
	elif not rno.isdigit():
		showwarning("Warning","Roll has to be numeric.")
		delete_window_ent_rno.delete(0,END)
		delete_window_ent_rno.focus()
	else:
		
		try:
			con = connect("akashproject.db")
			cursor=con.cursor()
			sql="delete from student where rno='%d'" 
			rno = int(delete_window_ent_rno.get())
			cursor.execute(sql % int(rno))
			if cursor.rowcount>0:
				showinfo('Success', 'Record deleted')
				con.commit()
			else:	
				showerror('Retry', 'Record doesnt exist')
			delete_window_ent_rno.delete(0,END)
		

		except Exception as e:
			showerror('Failure', e)
			con.rollback()
		finally:
			if con is not None:
				con.close()

#charts button ke liye


def f13():                                  #charts open main close(main ka charts button dabaya tho)

	main_window.configure(background='black')
	main_window_btn_charts.configure(background='yellow')
	names=[]
	marks=[]
	con = None
	try:
		con = connect('akashproject.db')
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		print(data)
		for d in data:
			names.append(d[1])
			marks.append(d[2])
			plt.bar( names,marks,color=['red','blue','orange','green'])
		plt.title("Batch Information!")
		plt.xlabel("Names")
		plt.ylabel("Marks")

		plt.show()
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f14():
	if askokcancel("Quit","Click OK to Quit"):
		main_window.destroy()








#main gui

splash = Tk()
splash.after(3000, splash.destroy)
splash.wm_attributes('-fullscreen', 'true')
msg = Label(splash, text="\nStudent Management System \nBy \nAkash Nair",font=('Calibri', 90, 'italic'))
msg.pack()
splash.mainloop()

main_window = Tk()
main_window.title("S. M. S.")
main_window.geometry("700x520+400+100")

main_window_btn_add = Button(main_window, text="Add", font=('Cambria', 20, 'bold'), width=10, command=f1)
main_window_btn_view = Button(main_window, text="View", font=('Cambria', 20, 'bold'), width=10, command=f5)
main_window_btn_update = Button(main_window, text="Update", font=('Cambria', 20, 'bold'), width=10, command=f6)
main_window_btn_delete = Button(main_window, text="Delete", font=('Cambria', 20, 'bold'), width=10, command=f9)
main_window_btn_charts = Button(main_window, text="Charts", font=('Cambria', 20, 'bold'), width=10, command=f13)

url = "https://ipinfo.io/"
res = requests.get(url)
data = res.json()
city_name = data['city']
a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
a2 = "&q=" + city_name
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
a = a1+a2+a3
res = requests.get(a)
data = res.json()
main = data['main']
avg = main['feels_like']
city_name = str(city_name)
avg = str(avg)
main_window_lbl_loct = Label(main_window, text=("Location: " + city_name + "\t\tTemp: " + avg + u'\u2103'),  font=('Cambria', 14, 'bold')) 
qt = requests.get("https://www.brainyquote.com/quote_of_the_day")
data = bs4.BeautifulSoup(qt.text,'html.parser')
info = data.find('img',{'class': 'p-qotd'})
main_window_lbl_qotd = Label(main_window, text=("QOTD: " +info['alt']), font=('Cambria', 12, 'bold'))




main_window_btn_add.pack(pady=10)
main_window_btn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_charts.pack(pady=10)
main_window_lbl_loct.pack(pady=10)
main_window_lbl_qotd.pack(pady=10)












#add gui

 

add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("500x600+400+100")

add_window_lbl_rno = Label(add_window, text="Enter rno:", font=('Cambria', 20, 'bold'))
add_window_ent_rno = Entry(add_window, bd=5, font=('Cambria', 20, 'bold'))
add_window_lbl_name = Label(add_window, text="Enter name:", font=('Cambria', 20, 'bold'))
add_window_ent_name = Entry(add_window, bd=5, font=('Cambria', 20, 'bold'))
add_window_lbl_marks = Label(add_window, text="Enter marks:", font=('Cambria', 20, 'bold'))
add_window_ent_marks = Entry(add_window, bd=5, font=('Cambria', 20, 'bold'))
add_window_btn_save = Button(add_window, text="Save", font=('Cambria', 20, 'bold'), command=f3)
add_window_btn_back = Button(add_window, text="Back", font=('Cambria', 20, 'bold'), command=f2)

add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
add_window.withdraw()









#view gui

view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("700x500+400+100")

view_window_st_data = ScrolledText(view_window, width=40, height=10, font=('Cambria', 20, 'bold'))
view_window_btn_back = Button(view_window, text="Back", font=('Cambria', 20, 'bold'), width=10, command=f4)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()









#update gui

update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("500x600+400+100")

update_window_lbl_rno = Label(update_window, text="Enter rno:", font=('Cambria', 20, 'bold'))
update_window_ent_rno = Entry(update_window, bd=5, font=('Cambria', 20, 'bold'))
update_window_lbl_name = Label(update_window, text="Enter new name:", font=('Cambria', 20, 'bold'))
update_window_ent_name = Entry(update_window, bd=5, font=('Cambria', 20, 'bold'))
update_window_lbl_marks = Label(update_window, text="Enter new marks:", font=('Cambria', 20, 'bold'))
update_window_ent_marks = Entry(update_window, bd=5, font=('Cambria', 20, 'bold'))
update_window_btn_save = Button(update_window, text="Save", font=('Cambria', 20, 'bold'), command=f8)
update_window_btn_back = Button(update_window, text="Back", font=('Cambria', 20, 'bold'), command=f7)

update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window.withdraw()








#delete gui

delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("500x600+400+100")

delete_window_lbl_rno = Label(delete_window, text="Enter rno:", font=('Cambria', 20, 'bold'))
delete_window_ent_rno = Entry(delete_window, bd=5, font=('Cambria', 20, 'bold'))
delete_window_btn_save = Button(delete_window, text="Save", font=('Cambria', 20, 'bold'), command=f11)
delete_window_btn_back = Button(delete_window, text="Back", font=('Cambria', 20, 'bold'), command=f10)

delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window.withdraw()







main_window.protocol("WM_DELETE_WINDOW", f14)
main_window.mainloop()
