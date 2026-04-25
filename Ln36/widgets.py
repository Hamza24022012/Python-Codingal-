from tkinter import *
from datetime import date

window=Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

lbl=Label(text="Here is product)",fg="white",bg="blue",height=1,width=300)

num1=Label(text="Enter 1st num",bg="#3895D3")
num1_entry=Entry()

num2=Label(text="Enter 2nd num",bg="#3895D3")
num2_entry=Entry()

def display():
    num1=int(num1_entry.get())
    num2=int(num2_entry.get())
    global product
    result= + num1 * num2
    product="product is " + str(result)
    text_box.insert(END,product)
    
text_box=Text(height=3)
btn=Button(text="Begin",command=display,height=1,bg="#3895D3",fg="white")

lbl.pack()
num1.pack()
num1_entry.pack()
num2.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()