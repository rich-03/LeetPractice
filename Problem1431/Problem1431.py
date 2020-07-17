from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        m = max(candies)

        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= m:
                ans.append(True)
            else:
                ans.append(False)

        return ans
