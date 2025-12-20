lower=int(input("enter the lowest number in the range"))
higher=int(input("enter the highest number in the range"))
print("prime numbers between",lower,"&",higher,"number are: ")

for num in range (lower,higher+1):
  
  if num>1:
   for i in range(2,num):
     if (num%i)==0:
      break
   else:
     print(num)
