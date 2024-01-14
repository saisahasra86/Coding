t=int(input())
while t>0:
    n=int(input())
    t-=1
    a=int(2000001)
    b=int(2000001)
    c=int(2000001)
    for i in range(0,n):
        mi, si = input().split()  # Read book number and binary string
        mi = int(mi)  # Convert book number to integer
        # si1 = int(si[0])  # First character of the binary string represents skill 1
        # si2 = int(si[1])  # Second character of the binary string represents 
        # print(si)
        if(si=="11"):
            a=min(a,mi)
        elif(si=="01"):
            b=min(b,mi)
        elif(si=="10"):
            c=min(c,mi)
        else :
            pass
    if(a==2000001):
        if(b==2000001 or c==2000001): print(-1)
        else: print(b+c)
    elif(b==2000001 or c==2000001): print(a)
    elif(a!=2000001 and b!=2000001 and c!=2000001): print(min(a,b+c))
    else : print(-1)

    
