from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, val in enumerate(nums):
            ans.insert(index[i], val)

        return ans
