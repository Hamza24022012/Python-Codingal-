print("enter your marks obtained in each subject")
math=int(input("please enter your marks in maths"))
english=int(input("please enter your marks in english"))
biology=int(input("please enter your marks in biology"))
chemistry=int(input("please enter your marks in chemistry"))
physics=int(input("please enter your marks in physics"))
business=int(input("please enter your marks in business"))
sum=math + english + biology + chemistry + physics + business
print ("sum of all subjects =",sum)
percentage= (sum/600)*100
print ("Your percentage is",percentage)
