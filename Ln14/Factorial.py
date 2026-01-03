def factorial(num):
    '''this is a recursive function to find factorial of a number'''
    if num==0 or num==1:
        return 1
    else:
     return num * factorial(num-1)
    
print(factorial.__doc__)
print("factorial of 0=",factorial(0))
print("factorial of 1=",factorial(1))
print("factorial of 4=",factorial(4))
print("factorial of 5=",factorial(5))
print("factorial of 100=",factorial(100))