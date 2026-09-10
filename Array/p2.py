"""Best Time to Buy and Sell Stock

Given an array of stock prices where prices[i] is the price on day i,
find the maximum profit from one buy and one sell transaction.

Includes:
1. Brute-force O(n^2) solution
2. Optimized O(n) solution
"""


class Solution:
    def maxProfit_bruteforce(self, prices: list[int]) -> int:
        """Check every valid buy/sell pair. Time: O(n^2), Space: O(1)."""
        maximum = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                maximum = max(maximum, profit)

        return maximum

    def maxProfit(self, prices: list[int]) -> int:
        """Track the lowest price so far. Time: O(n), Space: O(1)."""
        if not prices:
            return 0

        lowest = prices[0]
        maximum = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]

            maximum = max(maximum, prices[i] - lowest)

        return maximum


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]

    print("O(n^2):", solution.maxProfit_bruteforce(prices))
    print("O(n):", solution.maxProfit(prices))
