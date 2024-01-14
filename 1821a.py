h=int(input())
while h>0:
    h-=1
    t=input()
    count1=count2=0
    y=0
    for i in range(len(t)):
        if(t[i]=='?'):
            if i==0:
                y+=9
            else:
                count1+=1
        else:
            count2+=1
    if(t[0]=='0'): print(0)
    elif(len(t)==1):
        if(t[0]=='?') : print(9)
        else: print(1)
    elif(count2==len(t) and t[0]!=0):
        print(1)
    else:
        if y==0:
            print(10**count1)
        else:
            print((10**count1)*y)

                

        
