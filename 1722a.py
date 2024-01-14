t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()
    s1='Timru'
    count=0
    s=sorted(s)
    if(len(s)==5):
        for i in range(len(s)):
            if(s[i]==s1[i]):count+=1
            else :
                print("no")
                break
        if(count==5 and len(s)==5):print("yes")
    else:
        print("no")
