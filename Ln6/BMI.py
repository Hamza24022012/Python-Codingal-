height=float(input("enter height in cm"))
weight=float(input("enter weight in kg"))

BMI= weight/(height/100) **2

print("you're BMI is ",BMI)

if BMI <=18.4:
    print("you're underweight")
elif BMI <=24.9:
    print("you're healthy")
elif BMI <=29.9:
    print("you're overweight")
elif BMI <=34.9:
    print("you're severely overweight")
elif BMI <=39.9:
    print("you're obese")
else:
       print("you're severely obese")