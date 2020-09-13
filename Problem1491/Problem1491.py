from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        mins = min(salary)
        maxs = max(salary)
        ttl = 0
        for i in salary:
            if i not in [mins, maxs]:
                ttl += i

        return ttl / (len(salary) - 2)
