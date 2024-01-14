t=int(input())
while t>0:
    t-=1
    n,k=[int(i) for i in input().split()]
    n=int(n)
    k=int(k)
    string=input()
    i=0
    count=0
    while i<n:
        if string[i]=='B':
            count+=1
            i+=k
            i-=1
        else: i+=1
    print(count)