try:
    age=int(input("enter your age"))
    if age<18:
        raise ValueError
    else:
        print("age is valid")
except ValueError:
    print("invalid age")

