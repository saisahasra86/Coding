t=int(input())
while t>0:
    t-=1
    n,k=(input().split())
    n=int(n)
    k=int(k)
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    #b should be re arranged in a way that c[i]>a[i]-k or c[i]<a[i]+k
    i=0
    j=0
    while i<n and j<n:
        if(b[j]>a[i]-k or b[j]<a[i]-k):
            (b[i],b[j])=(b[i],b[j])
            b.insert(i,b[j])
            b.insert(j,b[i])
            print(b)
            i+=1
            j+=1
        else:
            j+=1
    print(b)



