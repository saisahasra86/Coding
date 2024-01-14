t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    count=0
    ans=-1
    prdt=1
    for i in range(n):
        if a[i]==0:
            count+=1
            continue
        prdt=prdt*a[i]
    if count>=2: print(0)
    elif count==1: print(prdt)
    else:
        for i in range(n):
            if a[i]!=0:
                ans=max((prdt//a[i])*(a[i]+1),ans)
        print(ans)
