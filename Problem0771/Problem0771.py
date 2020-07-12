class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for j in J:  # j stands for jewels
            for s in S:  # s stands for stones
                if j == s:
                    count += 1
        return count
