from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        for i in range(n):
            ans.append("Push")
            if i + 1 not in target:
                ans.append("Pop")
            if i + 1 == target[-1]:
                break

        return ans
