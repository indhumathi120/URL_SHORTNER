from tkinter import *
import pyshorteners
def link():
    name=e.get()
    short=pyshorteners.Shortener()
    x=short.tinyurl.short(name)
    var.set(x)


app=Tk()
app.title("Link Shortner")
var=StringVar()
l=Label(app, text=" Copy the link ")
e=Entry(app)
b1=Button(app, text="Convert", width=25, command=link)
l2=Entry(app, textvariable=var)
l.grid(row=1,column=0)
e.grid(row=1,column=1)
b1.grid(row=1,column=2)
l2.grid(row=2,column=1)
app.mainloop()
