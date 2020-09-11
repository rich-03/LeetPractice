from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        a = 1
        b = len(A)
        for i in range(0, b, 2):
            if A[i] % 2 == 1:
                while a < b and A[a] % 2 == 1:
                    a += 2
                A[i], A[a] = A[a], A[i]

        return A
