t=int(input())
while t>0:
    t-=1
    s=[]
    t1=input()
    for i in range(8):
        s.append(input())
    flag=0
    for i in range(8):
        count1=0
        for j in range(8):
            if(s[i][j]=='R'):
                count1+=1
        if(count1==8):
            flag=1
            print('R')
            break
    if(flag==0):
        for j in range(8):
            count1=0
            for i in range(8):
                if s[i][j]=='B':
                    count1+=1
            if count1==8 :
                print('B')
                break

    

                
