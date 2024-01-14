j=-1
arr=[3,5,0,0,4]
n=5
temp=0
for i in range(len(arr)):
    if(arr[i]==0):
        j=i
        break
if(j==-1): print(0)
for i in range(j+1,n):
    if arr[i]!=0:
            # swap(arr[i],arr[j])
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j+=1
print(arr)