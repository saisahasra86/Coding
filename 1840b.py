t=int(input())
while t>0:
    t-=1
    n,k=input().split()
    n=int(n)
    k=int(k)
    cost=0
    for i in range(k):
        cost+=2**i
    if(cost>n): print()
    else :

