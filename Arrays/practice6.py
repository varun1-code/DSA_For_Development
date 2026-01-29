#remove of duplicate from sorted array using 2 pointer method 
def remove_duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    arr=arr[:i+1]
    return arr
arr=[1,2,2,3,4,4,5,5,5,5,6]
obj=remove_duplicates(arr)
print("array after removing duplicates is:",obj)