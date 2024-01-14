t=int(input())
while t>0:
    t-=1
    s=input()
    s1="codeforces"
    count=0
    for i in range(0,len(s)):
        if(s[i]!=s1[i]):
            count+=1
    print(count)

