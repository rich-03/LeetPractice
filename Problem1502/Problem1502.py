from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            b = arr[i] - arr[i + 1]
            if a == b:
                continue
            else:
                return False

        return True
