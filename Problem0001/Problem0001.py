from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for n in enumerate(nums):
            if target - n[1] in d:
                return [d[target - n[1]], n[0]]
            else:
                d.update({n[1]: n[0]})

assert (Solution().twoSum([2, 7, 11, 15], 9) == [0, 1])
assert (Solution().twoSum([2, 7, 11, 15, 1], 3) == [0, 4])
