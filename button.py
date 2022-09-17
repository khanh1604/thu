from tkinter import *
root =Tk()

def click():
    
    label_1=Label(root)
    label_1.pack()
button1=Button(root,text = "Enter your name",command=click)
button1.pack()

root.mainloop()