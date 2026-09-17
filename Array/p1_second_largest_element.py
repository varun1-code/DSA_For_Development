"""Second Largest Element

Given an integer array, find the second largest distinct value.

Approach: single pass, tracking the largest and second-largest values seen
so far. Handles arrays with fewer than two elements and arrays with no
distinct second-largest value by returning -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return -1  # Not enough elements for a second largest

        first = second = float('-inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num

        return second if second != float('-inf') else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.secondLargest([3, 7, 2, 9, 4]))  # Output: 7
