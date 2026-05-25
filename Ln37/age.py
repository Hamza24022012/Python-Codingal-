from tkinter import *

window = Tk()
window.title("Age Calculator")
window.geometry("400x400")

frame = Frame(window)
frame.pack()

# Labels
l1 = Label(frame, text="Enter Name")
l2 = Label(frame, text="Enter Date")
l3 = Label(frame, text="Enter Month")
l4 = Label(frame, text="Enter Year")

# Entry Boxes
e1 = Entry(frame)
e2 = Entry(frame)
e3 = Entry(frame)
e4 = Entry(frame)

# Function
def calculateAge():
    name = e1.get()
    date = e2.get()
    month = e3.get()
    year = int(e4.get())

    age = 2025 - year

    message = f"Your name is {name}.\n"
    message += f"You were born on {date}/{month}/{year}.\n"
    message += f"Your age is {age} years."

    text.delete("1.0", END)
    text.insert(END, message)

# Text Box
text = Text(frame, height=5, width=40)

# Button
button = Button(
    frame,
    text="Calculate Age",
    bg="orange",
    command=calculateAge
)

# Packing
l1.pack()
e1.pack()

l2.pack()
e2.pack()

l3.pack()
e3.pack()

l4.pack()
e4.pack()

button.pack(pady=10)
text.pack()

window.mainloop()