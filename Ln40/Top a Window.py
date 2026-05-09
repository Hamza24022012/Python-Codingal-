from tkinter import *

window=Tk()
window.title("main")
window.geometry("600x500")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2=Label(top, text="Toplevel window")
    l2.pack()
    top.mainloop()

l=Label(window, text="Root window")
btn=Button(window, text="click to open another window",command=topwin)

l.pack()
btn.pack()

window.mainloop()