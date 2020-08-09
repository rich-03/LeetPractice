from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        a = []
        s = []
        for i in A:
            for j in i[::-1]:
                if j is 0:
                    s.append(1)
                else:
                    s.append(0)
            a.append(s)
            s = []

        return a
