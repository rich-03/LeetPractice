from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        x = []
        y = []
        for i in matrix:
            x.append(min(i))
        for j in zip(*matrix):
            y.append(max(j))

        return set(x) & set(y)
