t=int(input())
while t>0:
    t-=1
    a,b,c=[int(i) for i in input().split()]
    a=int(a)
    b=int(b)
    c=int(c)
    if(a+b>=10 or b+c>=10 or a+c>=10):
        print("Yes")
    else:
        print("No")