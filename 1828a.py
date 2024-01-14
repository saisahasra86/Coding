t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[]
    i=1
    while i<=n:
        y=2*i
        i+=1
        a.append(y)
    print(" ".join(map(str, a)))






