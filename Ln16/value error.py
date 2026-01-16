try:
    num=int(input("enter a number:"))
    print("number entered is:",num)
except ValueError as e:
    print("exception is:",e)