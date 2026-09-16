# Problem: Maximum Sum of Three Consecutive Elements
#
# Find the maximum sum of any 3 consecutive elements.

arr = [2, 5, 1, 8, 3, 7]

x = arr[0]
maximum = 0

for i in range(1, len(arr) - 1):
    maximum = max(maximum, x + arr[i] + arr[i + 1])
    x = arr[i]

print(maximum)

# Output: 18
# Time Complexity: O(n)
# Space Complexity: O(1)

# Learning:
# Maintain the previous element and calculate the sum of 3 consecutive elements.
# This builds the running-sum intuition used in later array problems.
