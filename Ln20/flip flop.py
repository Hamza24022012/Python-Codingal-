def palindrome(t):
    e=len(t)-1
    s=0
    while s<e:
        if t[s] != t[e]:
            return  False
        s=s+1
        e=e-1
    return True
t=(1,2,3,3,2,1)
if palindrome(t):
    print("tuple is flip flop")
else:
    print("tuple is flip flop")