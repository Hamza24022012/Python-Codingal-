print("select your ride")
print("1.Motorbike")
print("2.Car")

choice=int(input("enter your choice"))
if choice==1:
    print("What type of bike")
    print("1.Cruiser")
    print("2.Sport/Touring")
    choice2 = int(input("enter your choice"))
    if choice2==1:
        print("you have selected Cruiser")
    else:
        print("you have selected Sport/Touring")

elif choice==2:
    print("What type of car")
    print("1.Sedan")
    print("2.SUV")
    choice3 = int(input("enter your choice"))
    if choice3==1:
     print("you have selected Sedan")
    else:
       print("you have selected SUV")
else:
   print("you hve selected wrong choice")