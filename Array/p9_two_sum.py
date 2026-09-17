"""Two Sum

Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.

Approach: hash map. While scanning, store each value's index; for every
element, check whether its complement (target - num) has already been seen.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twosum(self, nums: list[int], target: int):
        seen = {}
        result = []
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                result.append([seen[compliment], index])
                del seen[compliment]
            else:
                seen[num] = index
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.twosum([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 7], 8)
    print(result)
