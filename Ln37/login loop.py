from tkinter import *

root=Tk()
root.title("Login")
root.geometry("400x300")

frame=Frame(master=root,width=360,height=200,bg='#d0efff')


lbl1=Label(frame,text="Full Name",bg="#3895D3",fg='white',width=12)
lbl2=Label(frame,text="Full Name",bg="#3895D3",fg='white',width=12)
lbl3=Label(frame,text="Full Name",bg="#3895D3",fg='white',width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

def display():
    name=name_entry.get()
    greet="Hey "+name
    message="\nCongrats for ur new account!"
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg="BEBEBE",fg="black")

btn=Button(text="Create Account",command=display,bg="red")



root.mainloop()