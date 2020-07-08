# Approach:
# two strings are anagrams if their canonical presentations (sorted lists of characters) are identical


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


assert(Solution().isAnagram("anagram", "nagaram") is True)
assert(Solution().isAnagram("rat", "car") is False)
