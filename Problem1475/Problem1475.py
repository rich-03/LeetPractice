from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, j in enumerate(prices):
            for c in prices[i + 1:]:
                if c <= j:
                    prices[i] = j - c
                    break
        return prices
