t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    a1=sorted(a)
    flag=0
    if len(a)==1: print("yes")
    for i in range(1,len(a)):
        if a1[i]<=a1[i-1]:
            print("no")
            flag=0
            break
        else :
            flag=1
    if flag==1 :  print("yes")
        
