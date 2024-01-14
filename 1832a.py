x=int(input())
while x>0 :
    x-=1
    s=input()
    count1=0
    if(len(s)==1 or len(s)==2) :  
        print("no")
        continue
    for i in range(0,((len(s))//2)-1):
        if (s[i]==s[i+1]):          
            count1+=1
        else:
            print("yes")
            break
    if(count1==((len(s)//2)-1)):       
        print("no")
