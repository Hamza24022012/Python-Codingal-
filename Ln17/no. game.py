import random
playing=True
number=random.randint(10,50)
print("guess the number 10-50")
while playing:
   guess=int(input("enter the number:"))
   if guess==number:
      print("you win")
      print("the number was",number)
      break
   else:
      print("Wrong ,try again")