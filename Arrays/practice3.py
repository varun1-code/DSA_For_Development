#find maximum and minum in array
def find_max_min():
    arr=[]
    x=int(input("enter the number of elments:"))
    for i in range(x):
        element=int(input("enter the elemensts:"))
        arr.append(element)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr[0],arr[-1],arr
minimum,maximum,array=find_max_min()
print("minimum is:",minimum)
print("maximum is:",maximum)
print("sorted array is:",array)
#-----------------------------------------------------------------------------

    