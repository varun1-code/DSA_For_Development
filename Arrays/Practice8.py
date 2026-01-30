#Left rotate array by K positions
#brute force approch
def left_roatate_array(arr,k):
    temp=arr[0:k]
    x=0
    for i in range(k,len(arr)):
        arr[i-k]=arr[i]
    for j in range(len(arr)-k,len(arr)):
        arr[j]=temp[x]
        x+=1
    return arr
arr=[1,2,3,4,5]
k=1
obj=left_roatate_array(arr,k)
print("array after left rotation by k positions is:",obj)