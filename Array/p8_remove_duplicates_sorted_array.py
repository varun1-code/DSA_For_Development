"""Remove Duplicates from Sorted Array

Given a sorted array, remove duplicates in-place so that each unique
value appears only once in the beginning of the array.

Example:
    Input:  [1, 1, 2, 2, 3, 4, 4]
    Output: [1, 2, 3, 4]

Approach: Two pointers
- i scans the array.
- j tracks the position of the last unique element.

Time Complexity: O(n)
Space Complexity: O(1)
"""


arr = [1, 1, 2, 2, 3, 4, 4]

i = 1
j = 0

while i < len(arr):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

    i += 1

print(arr[:j + 1])

# Output: [1, 2, 3, 4]

# Explanation:
# Since the array is sorted, duplicate values are next to each other.
# j points to the last unique value, while i scans every element.
# When arr[i] is different from arr[j], it is a new unique value.
# Move j forward and copy that value to arr[j].
#
# Trace:
# Start: i=1, j=0 -> [1, 1, 2, 2, 3, 4, 4]
# i=1: 1 == 1 -> duplicate, do nothing
# i=2: 2 != 1 -> j=1, arr[1]=2
# i=3: 2 == 2 -> duplicate, do nothing
# i=4: 3 != 2 -> j=2, arr[2]=3
# i=5: 4 != 3 -> j=3, arr[3]=4
# i=6: 4 == 4 -> duplicate, do nothing
#
# j + 1 = 4 unique elements.
# The first four positions contain: [1, 2, 3, 4]
