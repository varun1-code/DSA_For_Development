#Move all zeros to the end
def move_zeros_to_end(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    return arr
arr=[0,1,0,3,12,0,5,0,0,7]
obj=move_zeros_to_end(arr)
print("array after moving zeros to the end is:",obj)
