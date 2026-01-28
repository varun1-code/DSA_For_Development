#Print array elements
def print_array_elements(arr):
    for i in arr:
        print(i, end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
arr=[1,2,3,4,5,6,7,8,9,10]
print_array_elements(arr)