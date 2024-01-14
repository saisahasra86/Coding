t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=input().split()
    for i in a:
        i=int(i)
    sum1=sum2=0
    for i in a:
        if(int(i)%2==0): sum1+=int(i)
        else: sum2+=int(i)
    if(sum1>sum2) : print("yes")
    else : print("no")
    