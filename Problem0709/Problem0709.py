class Solution:
    def toLowerCase(self, str: str) -> str:
        l = ""
        for i in range(len(str)):
            s = ord(str[i])
            if 65 <= s <= 90:
                l += chr(s + 32)
            else:
                l += chr(s)
        return l
