from tkinter import *
from tkinter.messagebox import showinfo
def BottomDownload():
    showinfo(
        title = "Informational",
        message = "Downloat Button Clicked"
    )
root = Tk()
root.title("button exit")
root.geometry("200x200")


exit_button = Button( root,text="Exit",
                     command=lambda: root.quit())
exit_button.pack(padx=10,pady=5)

d = PhotoImage(file="C:/Users/trand/gui in python/invetive/download.png")
download_button= Button(root,image=d,text="Downloat",compound=LEFT,command = BottomDownload)
download_button.pack(expand = True,padx=10,pady=10)
root.mainloop()