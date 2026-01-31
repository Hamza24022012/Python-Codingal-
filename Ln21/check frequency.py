test_dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("original dictionary is",test_dict)
frequency_of_2=2
count=0

for key in test_dict:
    if test_dict[key]==frequency_of_2:
        count=count+1
print("The number of times two is coming is",count)