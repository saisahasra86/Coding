t=int(input())
while t>0:
    t-=1
    n=int(input())
    s1=input()
    L=''
    c=s1[0]
    i=1
    while i<n:
        if(s1[i]==c):
            L+=(s1[i])
            if i==len(s1)-1:
                break
            c=s1[i+1]
            i+=2
        else:
            i+=1
    print(L)



