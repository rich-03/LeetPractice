class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num = num / 2
                steps += 1
            else:
                num = num - 1
                steps += 1
        return steps


assert (Solution().numberOfSteps([14]) == [6])
assert (Solution().numberOfSteps([8]) == [4])
assert (Solution().numberOfSteps([123]) == [12])
