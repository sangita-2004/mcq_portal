from tkinter import *
from tkinter import messagebox
import pymysql
#print(dir(tkinter))

win = Tk ()
def Login():
	username = uid.get ()
	password = pwd.get ()
	print (username,"",password)
	conobj = pymysql.connect(host = 'localhost',user = 'root', password='',port= 3306)
	curobj = conobj. cursor()
	curobj.execute('use BCA2021AB;')
	test = f'select * from INFO where userid = "{username}" and password = "{password}";'
	curobj.execute(test)
	record = curobj.fetchall ()
	if len (record) :
		messagebox.showinfo("logininfo","welcome to home page")
		win.destroy()
		from mcq import myQuiz
		quiz = myQuiz()
	else :
		messagebox.showinfo("logininfo","sorry!!! Try Again....Try next Time")
def Reset():
	uid.delete(0,END)
	pwd.delete(0,END)	
def newUser():
	win.destroy()
	win1= Tk()
	def Submit():
				a= nuid.get()
				b=nphno.get()
				c=menu.get()
				d= var1.get()
				e= npwd.get()
				#print(a,"",b,"",c,"",d,"",e)
				conobj = pymysql.connect(host="localhost",user="root",password="",port=3306)
				curobj=conobj.cursor()
				#curobj.execute('create database BCA2021AB;')
				curobj.execute('use BCA2021AB;')
				#curobj.execute('create table INFO(userid varchar(20),phno bigint(10),dept varchar(20),gender varchar(6),password varchar(10));')
				r='insert into INFO values("{userid}","{phno}","{dept}","{gender}","{password}");'
				r1=r.format (userid=a,phno=b,dept=c,gender=d,password=e)
				#print(r1)
				curobj.execute(r1)
				conobj.commit()
				curobj.close()
				conobj.close()
				win1.destroy()
	def Reset():
		nuid.delete(0,END)
		nphno.delete(0,END)
		menu.set(None)
		#menu.delete(0,END)
		#var1.delete(0,END)
		var1.set (None)
		npwd.delete(0,END)

	win1.title("SignUp page")
	win1.maxsize(700,700)
	win1.minsize(700,700)

	Label (win1,text="please Sign UP Here",font=('Bernad MT',20,),fg="white",bg="hot pink",relief=RAISED,width=30).place(x=110,y=50)

	Label (win1,text="Set User ID",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=150)
	nuid = Entry(win1,font=('Bernard MT',15),bg="hot pink",fg="white")
	nuid.place(x = 350,y= 150)


	Label (win1,text="Enter Phone number",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=250)
	nphno = Entry (win1,font=('Bernad MT',15),bg="hot pink",fg="white")
	nphno.place(x = 350,y= 250)

	Label (win1,text="Select Dept number",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=350)
	menu=StringVar()
	drop=OptionMenu(win1,menu,"BCA","BSc.ITM","BSc.CS")
	drop.place(x = 450,y= 350)

		
	Label (win1,text="Select Gender",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=450)
	var1=StringVar(win1,None)
	Radiobutton(win1,text="Male",variable=var1,value="M",font=('Bernad MT',15,)).place(x = 350,y= 450)
	Radiobutton(win1,text="Female",variable=var1,value="F",font=('Bernad MT',15,)).place(x = 450,y= 450)

	Label (win1,text="Enter new password",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=550)
	npwd = Entry (win1,font=('Bernad MT',15),bg="hot pink",fg="white")
	npwd.place(x = 350,y= 550)
	
	Button(win1,text="Submit",font=('Bernard MT',15),bg="green",fg="white",command=Submit).place(x=200,y=600)
	Button(win1,text="Reset",font=('Bernard MT',15),bg="white",fg="blue",command=Reset).place(x=500,y=600)
	win1.mainloop()

def Exit():
	win.destroy()

win.title("Home page")
win.maxsize(700,700)
win .minsize(700,700)

Label (win,text="please Login Here",font=('Bernad MT',20,),fg="white",bg="blue",relief=RAISED,width=30,height=1).place(x=120,y=50)


Label (win,text="Enter User ID",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=110,y=150)
uid = Entry(win,font=('Bernard MT',15),bg="blue",fg="white")
uid.place(x = 350,y= 150)


Label (win,text="Enter Pssword",font=('Bernad MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=110,y=250)
pwd = Entry (win,font=('Bernad MT',15),bg="blue",fg="black")
pwd.place(x = 350,y= 250)

Button(win,text="login",font=('Bernard MT',15),bg="#AF69EF",fg="black",command= Login,activebackground="#c0c0c0").place(x=200,y=400)
Button(win,text="Reset",font=('Bernard MT',15),bg="#AF69EF",fg="black",command= Reset,activebackground="#c0c0c0").place(x=400,y=400)
Button(win,text="Sign Up",font=('Bernard MT',15),bg="#AF69EF",fg="black",command= newUser,activebackground="#c0c0c0").place(x=200,y=500)
Button(win,text="Exit",font=('Bernard MT',15),bg="#AF69EF",fg="black",command= Exit,activebackground="#c0c0c0").place(x=400,y=500)

win.mainloop ()