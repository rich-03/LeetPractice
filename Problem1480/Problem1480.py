from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        a = 0

        for i in nums:
            a += i
            ans.append(a)
        return ans
