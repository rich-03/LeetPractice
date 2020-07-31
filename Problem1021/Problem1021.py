class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        count = 0

        for i in S:
            if i is "(":
                if count > 0:
                    ans += i
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans += i

        return ans
