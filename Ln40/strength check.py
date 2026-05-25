from tkinter import *

root=Tk()
root.title("Password Strength Checker")
root.geometry("500x500")

l1=Label(root,text='Enter your password',bg='light blue')
e1=Entry(root, show="*")

# Create the display box outside the function so it doesn't duplicate
text_display = Text(root, height=4, width=30)

def strengthChecker():
    password=e1.get()
    length = len(password)
    
    # Clear previous results
    text_display.delete('1.0', END)
    
    if length <= 5:
        message="password strength is WEAK"
        color="red"
    elif length <= 8:
        message="password strength is MEDIUM"
        color="yellow"
    elif length <= 12:
        message="password strength is STRONG"
        color="light green"
    else:
        message="password strength is VERY STRONG"
        color="dark green"

    # Update the existing text box
    text_display.config(bg=color)
    text_display.insert(END, message)

button=Button(root,text="Check Strength",bg="red",command=strengthChecker)

# --- JOINED PACK SECTION ---
l1.pack(pady=10)
e1.pack(pady=5)
button.pack(pady=20)
text_display.pack(pady=10)

root.mainloop()
