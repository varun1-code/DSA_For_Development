# Problem: Find the Largest Element
#
# Given an integer array, find the largest element.

nums = [3, 7, 2, 9, 4]

largest = nums[0]

for i in range(1, len(nums)):
    if largest < nums[i]:
        largest = nums[i]

print(largest)

# Output: 9
# Time Complexity: O(n)
# Space Complexity: O(1)

# Learning:
# Keep track of the best (largest) value seen so far while traversing the array.
