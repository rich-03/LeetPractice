class Solution:
    def generateTheString(self, n: int) -> str:
        a = ''
        if n % 2 is 0:
            a = 'x' * (n - 1)
            a += 'y'
        else:
            a = 'x' * n

        return a
