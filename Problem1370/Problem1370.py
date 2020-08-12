class Solution:
    def sortString(self, s: str) -> str:
        a = sorted(set(s))
        ans = ""
        while s:
            for i in a:
                if i in s:
                    ans += i
                    s = s.replace(i, "", 1)
            for i in a[::-1]:
                if i in s:
                    ans += i
                    s = s.replace(i, "", 1)

        return ans
