t=int(input())
while t>0:
    t-=1
    n=int(input())
    L=[]
    count=-1
    while n!=0:
        count+=1
        if(n%10!=0):
            L.append((10**count)*(n%10))
        n=n//10
    if not L:
        print("1")
        print(n)
    else:
        print(len(L))
        for i in L:
            print(i,end=' ')
        print()

