from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(A[j][i] > A[j + 1][i] for j in range(len(A) - 1)) for i in range(len(A[0])))
