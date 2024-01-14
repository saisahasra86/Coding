
t=int(input())
while t>0:
    t-=1
    n,m=map(int,input().split())
    def nothing(n,m):
        if(n==m) : return True
        elif(n%3!=0 or m>n): return False
        else:
            return nothing(n/3,m) or nothing(2*(n/3),m)
    if(nothing(n,m)==True): print("yes")
    else: print("no")

            
            
