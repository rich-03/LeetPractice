class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = {'L': 0, 'R': 0}
        ans = 0

        for i in s:
            count[i] += 1

            if count['L'] == count['R']:
                ans += 1

                count['L'] = 0
                count['R'] = 0

        return ans
