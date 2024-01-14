t=int(input())
while t>0:
    t-=1
    n,k= input().split()
    n=int(n)
    k=int(k)
    l=[int(i) for i in input().split()]
    List=[]
    for i in range(n-k,n):
        List.append(l[i])
    for i in range(0,n-k):
        List.append(l[i])
    print(List)