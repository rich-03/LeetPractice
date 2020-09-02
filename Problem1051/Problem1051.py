from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        arr = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                heights[i] = arr[i]
                ans += 1

        return ans
