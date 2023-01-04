# File explorer
This is file explorer for windows 10 , made fully in python 3.6

# Functions:-

## For deleting folders or files
```
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
```

## For executing files
```
def show_opt():
	file = ent.get()+"/"+g.get(g.curselection()[0])
	os.startfile(file)
```

## For clearing File listbox
```
def cllt():
	g.delete("0",END)
```

## For copying the path of file or folder
```
def btn_copy_fun():
	t.clipboard_clear()
	t.clipboard_append(ent.get())
```
  
## For creating file
```
def c_n_flr():
	try:
		f = sd.askstring("File","Enter filename.")
		os.mkdir(ent.get()+"/"+f)
		msg.showinfo("File","New directory is created.")
		cllt()
		btn_path_fun()
	except:
		msg.showerror("Error","Not able to make new directory.")
```

## For copying file
```
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
```

## For deleting selected file
```
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
```

## Filling the file listBox
```
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
```

# Demo (For Windows 8 | 10 | 11)
* Download file from [here](http://github.com/abhineetraj1/file-explorer/raw/main/app.exe)
* Run app.exe file

# Programming language used
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>

## Author
*	[abhineetraj1](http://github.com/abhineetraj1)
