from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        max_price = 0
        low = prices[0]
        high = prices[0]
        for p in prices:
            if p < low:
                low = p
            if p - low > max_price:
                max_price = p - low

        return max_price