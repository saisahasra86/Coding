t=int(input())
while t>0:
    t-=1
    string=input()
    if(string[0]=='a' or string[1]=='b' or string[2]=='c'):
        print('Yes')
    else:
        print('No')