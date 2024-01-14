t=int(input())
while t>0:
    t-=1
    a,b,c=[int(i) for i in input().split()]
    a=int(a)
    b=int(b)
    c=int(c)
    count1=0
    count2=0
    if a==b: print(0)
    while a!=b:
        if a>b:
            if(a-b<2*c):

            a-=c
            b+=c
            count1+=1
             
        else:
            a-=c
            b+=c
            count2+=1
    if count1==0: print(count2)
    elif(count2==0): print(count1)


