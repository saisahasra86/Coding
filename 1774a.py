t=int(input())
while t>0:
    t-=1
    n=int(input())
    y=input()
    count=0
    for i in range(n):
        if(y[i]=='1'):
            count+=1
    if(count%2==0):
        p=count//2
    else :
        p=count//2+1
    if(y[0]=='1'):
        p-=1
    s=''
    for i in range (1,n):
        if(y[i]=='0'):
            s+='+'
        else :
            if(p!=0):
                s+='+'
                p-=1
            else :
                s+='-'
    print(s)

        


