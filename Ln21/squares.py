def square_filter(start,end):
    squares=[]
    even=[]
    odd=[]
for num in range(start,end+1):
    sq=num**2
    squares.append(sq)
    if sq % 2==0:
        even.append(sq)
    else:
        odd.append(sq)