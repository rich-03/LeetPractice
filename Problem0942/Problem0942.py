from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        a = len(S)
        b = 0
        ans = []
        for c in S:
            if c == "I":
                ans.append(b)
                b += 1
            if c == 'D':
                ans.append(a)
                a -= 1
        ans.append(b)
        return ans
