t=int(input())
while t>0:
    t-=1
    L=[]
    count=0
    for i in range(10):
        L.append(input())
    # print(L)
    matrix=[[1,1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1]]
    for i in range(10):
        for j in range(10):
            if L[i][j]=='X':
                count+=matrix[i][j]
    print(count)


    
