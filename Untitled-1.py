x=int(input())
List1=[]
List2=[]
count1=0
count2=0
count3=0
count4=0
while x>0 :
    s=input()
    if (len(s)%2)==0:
        for i in range(0,len(s)):
            x=s.count(s[i]) 
            List1.append(x) 
        for i in range(0,(len(List1)//2)):
            for j in range(0,(len(List1)//2)):
                if (List1[i]==List1[j]) :
                    count3+=1
                else :
                    count4+=1
        if(count3==len(List1)//2):
            print("no")
        else :
            print("yes")
    else :
        for i in range(0,len(s)):
            x2=s.count(s[i])
            List2.append(x2)
        for i in range(0,len(List2)//2):
            for j in range(0,len(List2)//2):
                if(List2[i]==List2[j]):
                    count1+=1
                else :
                    count2+=1
        if (count1==len(List2)):
            print("no")
        else :
            print("yes")

