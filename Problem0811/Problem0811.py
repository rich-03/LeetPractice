from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        dict = {}
        ans = []
        for d in cpdomains:
            arr = d.split(" ")
            count = int(arr[0])
            sub = arr[1].split(".")

            for i in reversed(range(len(sub))):
                temp = ".".join(sub[i:])

                if not dict.get(temp):
                    dict[temp] = count
                else:
                    dict[temp] += count

        for k in dict.keys():
            ans.append(str(dict[k]) + " " + k)

        return ans
