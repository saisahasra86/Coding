
# t=int(input())
# while t>0:
#     t-=1
#     n=int(input())
#     arr=[int(i) for i in input().split()]
#     stack=[]
#     n=len(arr)
#     stack.append(arr[n-1])
#     L=[]
#     L.append(-1)
#     for i in range(len(arr)-2,-1,-1):
#         if(arr[i]<arr[i+1]):
#             L.append(arr[i+1])
#             stack.append(arr[i+1])
#         else:
#             while stack and stack[-1]<=arr[i]:
#                 stack.pop()
#             if(len(stack)==0): L.append(-1)
#             else:    L.append(stack[-1])       
#     print(L[::-1])
n=4
a=[11,9,5,6]
maap={}
for i in range(n):
    maap[a[i]]=i
ma=dict(sorted(maap.items()))
print(ma)
ans=0
prev_index=0
for v in ma.values():
    print(v)
    ans+=abs(prev_index-v)
    prev_index=v
    print(ans)
print(ans)

       



