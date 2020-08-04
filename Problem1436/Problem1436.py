from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departCity = set()
        destCity = []
        for i in paths:
            if i[1] not in departCity:
                destCity.append(i[1])
            if i[0] in destCity:
                destCity.remove(i[0])
            departCity.add(i[0])

        return destCity[0]


