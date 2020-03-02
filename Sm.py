from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle

root=Tk( ) 
root.title(" student management system")
root.geometry("400x300+350+250")

adst=Toplevel(root)
adst.title("add student")
adst.geometry("400x300+350+250")
adst.withdraw( )

lblAddron = Label(adst , text ="Enter rno ")
lblAddron.pack( )
entAddrno = Entry(adst , bd=5)
entAddrno.pack( )

lblAddname = Label(adst , text ="Enter name ")
lblAddname.pack( )
entAddname = Entry(adst , bd=5)
entAddname.pack( )

def f5( ):
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		
		if  int(entAddrno.get( )) > 0:
			rno=int(entAddrno.get( ))
		else:
			
			messagebox.showerror("Issue ",'Give  postive number only in rno')
		
		if entAddname.get( ).isalpha( )== True:
			name=entAddname.get ( )
			if  int(len(name) ) > 1:
				cursor=con.cursor( )
				sql="insert into student values('%d ' , '%s')"
				args=(rno,name)
				cursor.execute(sql % args)
				con.commit( )
				msg=str(cursor.rowcount)+"inserted"
				entAddname.delete(0,END)
				entAddrno.delete(0,END)
				messagebox.showinfo("Success ",msg)
			else :
				messagebox.showerror("Issue ",'Give minimum two character in 				name ')
		else:
			messagebox.showerror("Issue ",'Give  character only in name ')
	
		
		

	except cx_Oracle.DatabaseError as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)

	except UnboundLocalError  as m:
		messagebox.showerror("Issue ",m)
	except ValueError  as t:
		messagebox.showerror("Issue ",t)
	
			
		

	finally:
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		


btnAddSave = Button(adst , text= "Save", command=f5)
btnAddSave.pack(pady=10 )


def f2( ):
	adst.withdraw( )
	root.deiconify( )
btnAddBack=Button(adst , text="Back", command=f2)
btnAddBack.pack(pady=10 )

def f1( ):
	root.withdraw( )
	adst.deiconify( )
btnAdd=Button(root , text="Add student", width =20 ,command=f1)
btnAdd.pack(pady=20 )

vist=Toplevel(root)
vist.title("View student")
vist.geometry("400x300+350+250")
vist.withdraw( )

def f3( ):
	root.withdraw( )
	vist.deiconify( )
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor( )
		sql="select * from student";
		cursor.execute(sql)
		data=cursor.fetchall( )
		#msg=" "
		st_list.config(state=NORMAL)
		st_list.delete(0,END)
		for row in data:
			#msg=msg+"rno: " + str(d[0])    +    "  name:  " +  d[1]   +"\n"
			st_list.insert(END,row,str(" "))
		st_list.config(state=DISABLED)
		
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Issue ",e)
		
	finally:
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )




btnView=Button(root, text="View student", width =20 ,command=f3)
btnView.pack(pady=20 )

stData=Scrollbar(vist)
stData.grid(row=0,column=1,sticky='ns' )

st_list=Listbox(vist,width=40,height=15,yscrollcommand=stData.set)
st_list.grid(row=0,column=0,padx=10)
stData.config(command=st_list.yview)




def f4( ):
	vist.withdraw( )
	root.deiconify( )
btnViewBack=Button(vist,text="Back",command=f4)
btnViewBack.grid( )

upst=Toplevel(root)
upst.title("Update student")
upst.geometry("400x300+350+250")
upst.withdraw( )


lblUpdateron = Label(upst , text ="Enter rno ")
lblUpdateron.pack( )
entUpdaterno = Entry(upst , bd=5)
entUpdaterno.pack( )

lblUpdatename = Label(upst , text ="Enter name ")
lblUpdatename.pack( )
entUpdatename = Entry(upst , bd=5)
entUpdatename.delete(0,END)
entUpdatename.pack( )


def f7( ):
	root.withdraw( )
	upst.deiconify( )
btnUpdate=Button(root , text="Update student", width =20 ,command=f7)
btnUpdate.pack(pady=20 )

def f8( ):
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		
		if  int(entUpdaterno.get( )) > 0:
			rno=int(entUpdaterno.get( ))
		else:
			messagebox.showerror("Issue ",'Give  postive number only in rno')

		if entUpdatename.get( ).isalpha( )== True:
			name=entUpdatename.get ( )
			if  int(len(name) ) > 1:
				cursor=con.cursor( )
				sql="update student set name='%s' where rno='%d' "
				args=(name,rno)
				cursor.execute(sql % args)
				con.commit( )
				msg=str(cursor.rowcount)+"updated"
				entUpdatename.delete(0,END)
				entUpdaterno.delete(0,END)
				messagebox.showinfo("Success ",msg)
			else :
				messagebox.showerror("Issue ",'Give minimum two character 				in name')
		else:
			messagebox.showerror("Issue ",'Give  character only in name ')
		

	except cx_Oracle.DatabaseError as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)

	except UnboundLocalError  as m:
		messagebox.showerror("Issue ",m)
		

	finally:
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		


btnUpdateSave = Button(upst , text= "Update",command=f8)
btnUpdateSave.pack(pady=10 )

def f6( ):
	upst.withdraw( )
	root.deiconify( )
btnUpdateBack=Button(upst , text="Back", command=f6)
btnUpdateBack.pack(pady=10 )

delst=Toplevel(root)
delst.title("Delete student")
delst.geometry("400x300+350+250")
delst.withdraw( )

lblDeleteron = Label(delst , text ="Enter rno ")
lblDeleteron.pack( )
entDeleterno = Entry(delst , bd=5)


entDeleterno.pack( )

def f9( ):
	root.withdraw( )
	delst.deiconify( )
btnDelete=Button(root , text="Delete student", width =20 ,command=f9)
btnDelete.pack(pady=20 )

def f10( ):

	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		
		rno=int(entDeleterno.get( ))
		cursor=con.cursor( )
		sql="delete from student where rno='%d' " 
		args=(rno)
		cursor.execute(sql%args)
		con.commit( )
		msg=str(cursor.rowcount)+"deleted"
		entDeleterno.delete(0,END)
		messagebox.showinfo("Success ",msg)

	except cx_Oracle.DatabaseError as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)

	
	except ValueError  :
		messagebox.showerror("Issue ",'only numbers are required!!!')
		

	finally:
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		

btnDeletedel = Button(delst , text= "Delete",command=f10)
btnDeletedel.pack(pady=10 )

def f11( ):
	delst.withdraw( )
	root.deiconify( )
btnDeleteBack=Button(delst , text="Back", command=f11)
btnDeleteBack.pack(pady=10 )



root.mainloop( )


