"""Move Zeroes

Given an array, move all zeroes to the end while keeping the relative
order of the non-zero elements, in-place.

Approach: two pointers.
- i scans every element.
- j tracks the position where the next non-zero value should go.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
