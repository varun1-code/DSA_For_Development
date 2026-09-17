"""Two Sum — Sorted Array

Given a sorted array and a target, find two numbers that add up to the
target and return their values (or indices).

Approach: two pointers.
- left starts at the beginning, right starts at the end.
- If the pair sum is too big, move right inward (decrease the sum).
- If the pair sum is too small, move left inward (increase the sum).
- Because the array is sorted, this converges in a single pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [2, 7, 11, 15]
target = 9

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total > target:
        right -= 1
    elif total < target:
        left += 1
    else:
        print(arr[left], arr[right])
        break

# Output: 2 7

# Learning:
# Sorting lets us decide which pointer to move based on whether the
# current sum is too high or too low, avoiding the O(n^2) brute-force
# pair check used when the array is unsorted (see p9_two_sum.py).
