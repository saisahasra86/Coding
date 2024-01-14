from math import gcd
def intial_no(n1,n):
    gcd_num=n1[0]
    for i in range(1,n):
        gcd_num=gcd(gcd_num,n1[i])

    for i in n1:
        if(i%gcd_num==0):
            return i
t=int(input())
while t>0:
    t-=1
    n=int(input())
    p=list(input().split())
    for i in p:
        i=int(i)
    intial=intial_no(p,n)
    print(intial)
