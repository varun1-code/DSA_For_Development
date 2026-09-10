class Solution:
    def findMinMax(self, nums: list[int]) -> tuple[int, int]:
        if not nums:
            return None, None  # Return None for both if the list is empty
        min_val = max_val = nums[0]
        for num in nums:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        return min_val, max_val