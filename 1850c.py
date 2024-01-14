t=int(input())
while t>0:
    t-=1
    L=[]
    for i in range(8):
        s=input()
        L.append(s)
    ans=''
    for i in range(len(L)):
        for j in range(len(L[0])):
            if(L[i][j]!='.'):
                ans+=L[i][j]
    print(ans)


    