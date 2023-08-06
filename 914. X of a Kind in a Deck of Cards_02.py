"""
Wrong Answer
67 / 74 testcases passed
Input
deck =
[0,0,0,0,0,1,1,1,1,1]

Use Testcase
Output
false
Expected
true
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        cnts = set(dic.values())
        if 1 in cnts: return False

        divs, q = {2,3}, min(cnts)
        for p in range(2, q//2+1):
            if q % p == 0:
                divs.add(p)

        for _, cnt in enumerate(cnts, 1):
            tmp = set()
            for d in divs:
                if cnt % d == 0:
                    tmp.add(d)
            divs = divs & tmp
            if not divs:
                return False
        return True