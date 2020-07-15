from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        count = 0
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1

        for i in dict:
            n = dict[i]
            count += (n*(n-1)//2)

        return count
