def add(P,Q):
    return P+Q

def sub(P,Q):
    return P-Q

def multi(P,Q):
    return P*Q

def div(P,Q):
    return P/Q

print("please select the operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")

choice = input("please enter your choice[a//b/c/d]")
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

if choice=="a":
    print(num1 , "+" , num2 , "=" ,add(num1,num2))

elif choice=="b":
    print(num1 , "-" , num2 , "=",sub(num1,num2))

elif choice=="c":
    print(num1 , "x" , num2 , "=",multi(num1,num2))

elif choice=="d":
    print(num1 , "/" , num2 , "=",div(num1,num2))

else:
    print("invalid input")