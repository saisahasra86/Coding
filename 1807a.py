t=int(input())
while t>0:
    t-=1
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if(a+b==c): print("+")
    else:
        if(a-b==c): print("-")

