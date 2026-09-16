# Problem: Maximum Subarray — Kadane's Algorithm
#
# Given an integer array, find the contiguous subarray (containing at least
# one number) with the largest sum and return that sum.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1, len(arr)):
    # Either start a new subarray at arr[i], or continue the current one.
    current_sum = max(arr[i], current_sum + arr[i])

    # Keep the best sum found anywhere in the array.
    maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)

# Output: 6
# Maximum-sum subarray: [4, -1, 2, 1]
# Time Complexity: O(n)
# Space Complexity: O(1)

# Core idea:
# current_sum represents the maximum sum of a subarray that ends at index i.
# If extending the previous subarray is worse than starting at arr[i], start fresh.
# We do not actually create a new array; we only reset current_sum conceptually.

# Trace:
# Start: current_sum = -2, maximum_sum = -2
# i=1:  current_sum = max(1, -2+1) = 1,  maximum_sum = 1
# i=2:  current_sum = max(-3, 1-3) = -2, maximum_sum = 1
# i=3:  current_sum = max(4, -2+4) = 4, maximum_sum = 4
# i=4:  current_sum = max(-1, 4-1) = 3, maximum_sum = 4
# i=5:  current_sum = max(2, 3+2) = 5, maximum_sum = 5
# i=6:  current_sum = max(1, 5+1) = 6, maximum_sum = 6
# i=7:  current_sum = max(-5, 6-5) = 1, maximum_sum = 6
# i=8:  current_sum = max(4, 1+4) = 5, maximum_sum = 6

# Important:
# Use range(1, len(arr)), not range(1, len(arr)-1), so the final element is processed.
