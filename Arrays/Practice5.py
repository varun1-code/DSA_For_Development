#finding second largest element in an array
def second_largest(arr):
    largest=-float('inf')
    second_largest=-float('inf')
    if len(arr)<2:
        return "array should have atleast two elements"
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    return second_largest
arr=[35]
obj=second_largest(arr)
print("second largest element is:",obj)
