med_c=input("do you have any medical issue YES or NO")
att=int(input("State your number of attendance days"))

if med_c=="YES":
    print("you are eligible")
else:
    if att>=75:
        print("you are eligible")
    else:
        print("you are ineligible")