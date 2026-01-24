L=[4,5,1,2,9,7,10,8]
print("orignal list is:",L)

sum=0
for i in L:
    sum=sum+i
avg=sum/len(L)
print("sum =",sum)
print("average =",avg)

L.sort()
print("smallest element",L[0])
print("biggest element",L[-1])