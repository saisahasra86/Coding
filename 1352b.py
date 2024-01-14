t=int(input())
while t>0:
    t-=1
    n,k=input().split()
    n=int(n)
    k=int(k)
    count=0
    p=n//k
    if(n%k==0):
        print("YES")
        print(k*(str(p)+' '))
    elif(n%2!=0 and k%2==0):
        print("NO")
    else:
        if n%2!=0 and p%2==0 :
                p=p-1
        elif(n%2==0):
            if(k%2!=0) and (p%2!=0):
                    p-=1
        if(p<=0 or n-(p*(k-1))<=0): print("NO")
        else: 
            print("YES")
            print(((str(p)+" ")*(k-1))+str(n-(p*(k-1))))


            
