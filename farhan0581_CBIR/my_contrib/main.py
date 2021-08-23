from save_data import Data_index
from search_img import Searcher
from index import Index
from search import Search
from Tkinter import *
import requests
from tkFont import Font
import tkMessageBox

par_color=0
par_orb=1

def call_index():
	global par_orb,par_color
	path= z.get()
	if path== '':
		tkMessageBox.showinfo('ERROR','Please folder path!!!')
	elif path != '':
		if par_orb==1:
			di=Data_index(path)
			di.insert_data()
		elif par_color==1:
			i=Index(path)
			i.main_fun()


def call_search():
	global par_orb,par_color
	info = v.get()
	path=z.get()
	if info=='':
		tkMessageBox.showinfo('ERROR','Please enter image name!!!')
	elif info !='':
		if par_orb==1:
			s=Searcher(info)
			s.search_image()
		elif par_color==1:
			path='/home/farhan/project/CBIR/my_contrib/index.csv'
			obj=Search(info,path)
			obj.main_search()


def cleartext():
	addr.delete(0,'end')
	srch_text.delete(0,'end')


def set_color():
	global par_orb,par_color
	par_color=1
	par_orb=0

def set_orb():
	global par_orb,par_color
	par_orb=1
	par_color=0

#GUI

# root = Tk().geometry("750x450")
root=Tk()
v=StringVar()
z=StringVar()
var=StringVar(root)

#menu button
menu_=Menu(root)
root.config(menu=menu_)
sub=Menu(menu_)
menu_.add_cascade(label="Select Method",menu=sub)
sub.add_command(label="COLOR_histogram",command=set_color)
sub.add_separator()
sub.add_command(label="ORB_features",command=set_orb)

label = Label(root)
label.pack()
tframe=Frame(root)
tframe.pack(side=TOP,pady=10,fill=X)
addrc=Label(tframe,text="CONTENT BASED IMAGE RETREIVAL SYSTEM",font=('bold'))
addrc.pack(pady=10)
addrc=Label(tframe,text="Enter the Path of Image folder",font=('bold'))
addrc.pack(pady=10)
addr=Entry(tframe,textvariable=z)
addr.pack(fill=X,padx=30)
btn=Button(tframe,text="Index DB",fg="red",bg="white",command=call_index)
btn.pack(pady=10,padx=300,side=LEFT)


#search

frame=Frame(root)
frame.pack()
srch=Label(frame,text="Enter query image name",font=('bold'))
srch.pack(pady=10)
srch_text=Entry(frame,textvariable=v)
srch_text.pack(fill=X,padx=30)
btn_ss=Button(frame,text="Search",fg="blue",bg="white",command=call_search)
btn_ss.pack(pady=10,padx=90,side=LEFT)

lframe=Frame(root)
lframe.pack()
cbtn=Button(lframe,text="Clear fields",fg="green",bg="white",command=cleartext)
cbtn.pack(pady=10,padx=20,side=LEFT)

mainloop()
