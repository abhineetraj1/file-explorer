from tkinter import *
from time import sleep as slp
import os
import random as rdm
import shutil as sl
import datetime as dt
from tkinter import simpledialog as sd
from tkinter import messagebox as msg
rdmc = rdm.choice(["green","blue","white","yellow","orange","pink","purple"])
def delete_mn_btn():
	pth=ent.get()+"/"+g.get(g.curselection()[0])
	try:
		if (os.path.isdir(pth) == True):
			sl.rmtree(pth)
			btn_path_fun()
			msg.showinfo("File","Folder is deleted.")
		else:
			os.remove(pth)
			msg.showinfo("File","File is deleted.")
			btn_path_fun()
	except:
		msg.showerror("File","Error while deleting.")
def show_opt():
	file = ent.get()+"/"+g.get(g.curselection()[0])
	os.startfile(file)
def cllt():
	g.delete("0",END)
def btn_copy_fun():
	t.clipboard_clear()
	t.clipboard_append(ent.get())
def c_n_flr():
	try:
		f = sd.askstring("File","Enter filename.")
		os.mkdir(ent.get()+"/"+f)
		msg.showinfo("File","New directory is created.")
		cllt()
		btn_path_fun()
	except:
		msg.showerror("Error","Not able to make new directory.")
def clet():
	ent.delete(0,END)
def des_btn():
	clet()
	cllt()
	path = "C:/Users/"+os.getlogin()+"/Desktop"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def mus_btn():
	cllt()
	clet()
	path = "C:/Users/"+os.getlogin()+"/Music"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def pic_btn():
	cllt()
	clet()
	path = "C:/Users/"+os.getlogin()+"/Pictures"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def vid_btn():
	cllt()
	clet()
	path = "C:/Users/"+os.getlogin()+"/Videos"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def down_btn():
	cllt()
	clet()
	path = "C:/Users/"+os.getlogin()+"/Downloads"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def doc_btn():
	cllt()
	clet()
	path = "C:/Users/"+os.getlogin()+"/Documents"
	try:
		s= os.listdir(path)
		n=0
		ent.insert("1",path)
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
def copy_fl():
	try:
		a=ent.get()+"/"+g.get(g.curselection()[0])
		b=ent.get()+"/"+str(dt.datetime.now()).replace(".","").replace(":","")+" - "+g.get(g.curselection()[0])
		if(os.path.isdir(a) == "True"):
			sl.copytree(a,b)
		else:
			sl.copy(a,b)
		btn_path_fun()
	except Exception as err:
		print(err)
		msg.showerror("Error","Error while copying")
def opn_fl():
	path=ent.get()+"/"+g.get(g.curselection()[0])
	if (os.path.isdir(path) == True):
		clet()
		ent.insert("1",path)
		cllt()
		btn_path_fun()
	else:
		show_opt()
		btn_path_fun()
def btn_path_fun():
	cllt()
	path = ent.get()
	try:
		s= os.listdir(path)
		n=0
		while(len(s)>n):
			g.insert(n,s[n])
			n=n+1
	except:
		msg.showerror("Error","Path not found")
t = Tk()
t.title("Abhineet Raj - FILE Explorer")
t.geometry("600x400")
bg= Label(t, height="400", width="500", background=rdmc)
lb = Label(t, text="Path", font=40, background=rdmc)
ent=Entry(font=40, width="35")
ent.insert("1",("C:/Users/"+os.getlogin()+"/Desktop"))
btn_ist=Button(t,command=btn_path_fun ,text="List",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_copy=Button(t,command=btn_copy_fun ,text="Copy",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_de = Button(t,command=des_btn ,text="Desktop",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_doc = Button(t,command=doc_btn ,text="Documents",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_pic = Button(t,command=mus_btn, text="Pictures",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_mus = Button(t,command=pic_btn, text="Music",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_vid = Button(t,command=vid_btn, text="Video",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn_down = Button(t,command=down_btn, text="Downloads",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn = Button(t,command=c_n_flr ,text="Create new Folder",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn1 = Button(t,command=delete_mn_btn, text="Delete",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn2 = Button(t,command=opn_fl, text="Open",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
btn5 = Button(t,command=copy_fl, text="Copy file",font=40 ,activebackground="green", activeforeground="white", background="white", relief="groove")
m = Scrollbar(t, orient="vertical")
g = Listbox(t, height=14, width=60, yscrollcommand=m.set)
m.configure(command=g.yview)
bg.place(x=0,y=0)
lb.place(x=0,y=350)
btn_ist.place(x=530,y=350)
btn_copy.place(x=450,y=350)
ent.place(x=50,y=350)
btn_de.place(x=0,y=0)
btn_doc.place(x=0,y=40)
btn_pic.place(x=0,y=80)
btn_mus.place(x=0,y=120)
btn_vid.place(x=0,y=160)
btn_down.place(x=0,y=200)
btn.place(x=170,y=230)
btn1.place(x=250,y=270)
btn2.place(x=170,y=270)
btn5.place(x=330,y=270)
g.place(x=135,y=0)
m.place(x=510,y=0)
t.mainloop()