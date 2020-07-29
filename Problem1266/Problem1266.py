from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x = points[0][0]
        y = points[0][1]
        ans = 0
        for i, group in enumerate(points):
            if i is 0: continue
            x = abs(x - group[0])
            y = abs(y - group[1])
            ans += max(x, y)
            x = group[0]
            y = group[1]

        return ans
