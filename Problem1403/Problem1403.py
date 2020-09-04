from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        ans = [nums.pop()]
        while sum(ans) <= sum(nums):
            ans.append(nums.pop())

        return ans
