import array as arr
num=arr.array('i',[1,3,4,5,3,7,8,3,9])
print("original array=",num)
print("number of times 3 is written",num.count(3))
num.reverse()
print("reverse order")
print(num)