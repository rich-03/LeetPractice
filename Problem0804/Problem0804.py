from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        u = set()
        for i in words:
            mc = ''
            for j in i:
                mc += mcode[ord(j) - 97]
            u.add(mc)

        return len(u)
