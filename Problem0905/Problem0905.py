from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e = []
        o = []
        for i in A:
            if i % 2 is 0:
                e.append(i)
            else:
                o.append(i)

        return e + o