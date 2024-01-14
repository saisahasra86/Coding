t=int(input())
while t>0:
    t-=1
    n=int(input())
    p=[int(i) for i in input().split()]
    p.sort()
    sum1=0
    if(n==1):
        print(0)
    elif(n%2==0):
            i=0
            j=n-1
            while i<n-1 and j>=1 and i<j:
                sum1+=abs(p[j]-p[i])
                # print(sum1)
                if i==j or i==j-1: break
                while ((i<n-1)and (p[i]==p[i+1])):
                    i+=1
                while ((j>=1) and (p[j]==p[j-1])):
                    j-=1
                if i==j or i==j-1: break
                i+=1
                j-=1
            print(sum1)
    else:
        i=0
        j=n-1
        while i<n-1 and j>=1 and i<j:
            sum1+=abs(p[j]-p[i])
            if i==j or i==j-1: break
            while((i<n-1) and (p[i]==p[i+1]) ):
                i+=1
            while((j>=1) and (p[j]==p[j-1])):
                j-=1
            if i==j or i==j-1 : break
            i+=1
            j-=1
        print(sum1)
         


    


    
