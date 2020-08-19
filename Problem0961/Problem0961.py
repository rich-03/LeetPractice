from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = Counter(A)
        for i, j in n.items():
            if j > 1:
                return i

        return A[-1]
