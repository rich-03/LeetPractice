from typing import List
from collections import Counter


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            c = Counter(i)
            for j, k in c.items():
                if j < 0:
                    count += k

        return count
