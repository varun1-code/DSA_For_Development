#Find the second largest element in an array
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