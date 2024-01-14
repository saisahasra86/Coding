t=int(input())
while t>0:
    t-=1
    n,p,k=input().split()
    n=int(n)
    p=int(p)
    k=int(k)
    if(n+p==k or k+p==n or n+k==p):
        print("yes")
    else :
        print("no")