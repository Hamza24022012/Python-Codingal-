from tkinter import *

root = Tk()
root.title("Interest Calculator")

def interestcalculator():
    try:
        # float() is safer than int() for money and rates
        amount = float(e1.get())
        rate = float(e2.get()) / 100
        time = float(e3.get())
        
        simpleInterest = amount * time * rate
        message = f"The Simple interest is {simpleInterest:.2f} \n"
        
        # Clears the box before showing new result
        text.delete('1.0', END)
        text.insert(END, message)
    except ValueError:
        text.delete('1.0', END)
        text.insert(END, "Please enter valid numbers")

# UI Elements
l1 = Label(root, text="Enter Principal Amount:")
e1 = Entry(root)

l2 = Label(root, text="Enter Rate of Interest (%):")
e2 = Entry(root)

l3 = Label(root, text="Enter Time (Years):")
e3 = Entry(root)

l4 = Label(root, text="Result:")
text = Text(root, height=3, width=30)

button = Button(root, text="Calculate", bg="red", fg="white", command=interestcalculator)

# Packing elements in order
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
l4.pack()
text.pack()
button.pack()

root.mainloop()
