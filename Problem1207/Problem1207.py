# Approach
# definition of unique occurences can be determined when length of values would be equal to length of a set of values


from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr).values()
        return len(count) == len(set(count))


assert (Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True)
assert (Solution().uniqueOccurrences([1, 2]) is False)
assert (Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True)
