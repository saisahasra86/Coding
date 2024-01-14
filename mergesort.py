def mergesort(arr):
    left=arr[0]
    n=len(arr)
    middle=n//2
    List1=[]
    List2=[]
    count=0
    for i in range(0,middle):  List1.append(arr[i])
    for i in range(middle,n):  List2.append(arr[i])
    if(len(List1)==0):  return List2
    if(len(List2)==0):  return List1
    #so as to it recursively call merge sort
    List1=mergesort(List1)
    List2=mergesort(List2)
    #merging needed
    final_list=[]
    i=0
    j=0
    while (i<len(List1) and j<len(List2)):
        if(List1[i]>List2[j]):
            final_list.append(List2[j])
            j+=1
        else:
            final_list.append(List1[i])
            i+=1
            count+=(middle-left+1)
    if(i==len(List1) and j<len(List2)):
        for k in range(j,len(List2)):
                final_list.append(List2[k])
    elif(i<len(List1) and j==len(List2)):
        for k in range(i,len(List1)):
            final_list.append(List1[k])
    return count
# def merge(arr,low,mid,high):
#     left=low
#     right=mid+1
#     l=[]
#     while left<=mid and right<=high:
#         if(arr[left]<=arr[right]):
#             l.append(arr[left])
#             left+=1
#         else:
#             l.append(arr[right])
#             right+=1
#     while (left<=mid):
#         l.append(arr[left])
#     while right<=high:
#         l.append(arr[right])
#     for i in range(low,high+1):
#         arr[i]=l[i-low]
#     return arr

# def merge_sort(L,low,high):
#     if low>=high : return 
#     middle=(low+high)//2
#     merge_sort(L,low,middle)
#     merge_sort(L,middle,high)
#     merge(L,low,middle,high)
#     return L
L=[3,4,5,2,1]
print(mergesort(L))