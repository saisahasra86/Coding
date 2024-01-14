#n lines input
n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
#nspaced integers in a line
a=input().split()
#method1
for i in range(n):
    a[i]=int(a[i])
#method2
a=[int(i) for i in a]
#method 3
a=set(map(int,a))

