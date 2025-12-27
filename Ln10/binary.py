num=int(input("Enter a decimal number:"))
binary = " "

while num > 0:
    remainder=num%2
    temp = ""

    for i in range(1):
        temp=str(remainder)

    binary= temp+binary
    num = num//2

print("binary number:",binary)