t=int(input())
while t>0:
    t-=1
    n=int(input())
    ans=-1
    for i in range(n):
        ai,bi=[int(i) for i in input().split()]
        ai=int(ai)
        bi=int(bi)
        if(ai<=10):
            if(ans<bi):
                h=i
                ans=bi
    print(h+1)
