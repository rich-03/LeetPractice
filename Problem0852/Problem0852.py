from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return [i for i in range(1, len(A) - 1) if A[i] > A[i + 1] and A[i] > A[i - 1]][0]
