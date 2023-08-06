"""
153 ms runtime beats 21.52%
16.6 MB memory beats 37.7%
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        cnts = set(dic.values())
        if 1 in dic.values(): return False
        if len(cnts) == 1: return True

        divs, q = set(), min(cnts)
        for p in range(2, q+1):
            if q % p == 0:
                divs.add(p)
        cnts.remove(q)

        for cnt in cnts:
            tmp = set()
            for d in divs:
                if cnt % d == 0:
                    tmp.add(d)
            if not tmp:
                return False
            divs = tmp
        return True