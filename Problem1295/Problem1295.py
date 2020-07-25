from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i)) % 2 is 0:
                ans += 1

        return ans
