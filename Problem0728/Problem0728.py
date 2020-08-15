from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if '0' not in str(i):
                for j in str(i):
                    if i % int(j) != 0:
                        break
                else:
                    ans.append(i)

        return ans



