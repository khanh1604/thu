from tkinter import *
root =Tk()
e = Entry()
e.pack()
e.insert(0,"Enter your name")
def click():
    var = "hello"+e.get()
    label_1=Label(root,text=var)
    label_1.pack()
button1=Button(root,text = "Enter your name",command=click)
button1.pack()

root.mainloop()