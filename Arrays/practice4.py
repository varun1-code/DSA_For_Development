#Reverse an Array
''''def reverse_array(arr):
    j=len(arr)-1
    for i in range(len(arr)):
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
        if i>=j:
            break
    return arr
arr=[1,2,3,4,5]
obj=reverse_array(arr)
print("reversed array is:",obj)'''
#---------------------------------------------------------------------
#using while loop
def reverse_array(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
arr=[1,2]
obj=reverse_array(arr)
print("reversed array is:",obj)