t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=input()
    mp={}
    flag=1
    for i in range(len(a)):
        if a[i] not in mp:
            mp[a[i]]=i
            # print(a[i])
        else:
            if((i-mp[a[i]])%2!=0):
                # print(a[i])
                print("no")
                flag=0
                break
    if(flag==1): print("yes")
                