class Solution:
    def maximum69Number(self, num: int) -> int:
        ans = num
        n = str(num)
        for i, j in enumerate(n):
            if j is '6':
                ans = max(ans, int(n[:i] + '9' + n[i + 1:]))

        return ans
