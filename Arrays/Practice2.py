# Sum of All Elements
def sum_of_elements():
    arr=[]
    sum=0
    x=int(input("enter the number of elements :"))
    for i in range(x):
        element=int(input("enter element :"))
        arr.append(element)
    for i in arr:
        sum+=i
    return sum

result=sum_of_elements()
print(result)
#-----------------------------------------------------------------------------
#another approach
def sum_of_array_elements(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
arr=[1,2,3,4,5]
result=sum_of_array_elements(arr)