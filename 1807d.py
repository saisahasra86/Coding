t=int(input())
while t>0:
    t-=1
    n,q=input().split()
    n=int(n)
    q=int(q)
    a=[int(i) for i in input().split()]
    default_value = 0  # Replace 0 with the desired default value
    prefsum = [default_value for _ in range(n+1)]
    for i in range(1,len(a)+1):
        prefsum[i]=prefsum[i-1]+a[i-1]
    while q>0:
        q-=1
        l,r,k=input().split()
        l=int(l)
        r=int(r)
        k=int(k)
        sum1=prefsum[l-1]+(r-l+1)*k+prefsum[n]-prefsum[r]
        if(sum1%2==0): print("no")
        else : print("yes")
    

