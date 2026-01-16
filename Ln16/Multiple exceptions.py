try:
    num1 , num2 = eval(input("enter 2 number separated by comma"))
    result=num1/num2
    print ("result is",result)
except ZeroDivisionError:
    print("division by 0 is error")
except SyntaxError:
    print("comma is missing,please add numbers separated by comma ")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will be excuted no matter what")