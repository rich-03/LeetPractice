from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [variable[0] for variable in sorted([(index, sum(row)) for index, row in enumerate(mat)], key=lambda value: value[1])[:k]]
