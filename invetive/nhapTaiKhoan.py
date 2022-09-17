from tkinter import *

win = Tk()
win.geometry("300x300")
win.title("Sign in")





inputE = Label(win,text="Email address")
fieldE = Entry(win,bd=5).grid(row=1)

win.mainloop()