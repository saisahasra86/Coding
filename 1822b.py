t=int(input())
while t>0:
    t-=1
    n=int(input())
    p=[int(i) for i in input().split()]
    L1=sorted(p)
    if(len(L1)==2):
        print(L1[0]*L1[1])
    else:
        if(L1[0]*L1[1]>L1[-1]*L1[-2]):
            print(L1[0]*L1[1])
        else:
            print(L1[-1]*L1[-2])
        



