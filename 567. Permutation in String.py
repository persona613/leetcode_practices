"""
64 ms runtime beats 77.89%
17.67 MB memory beats 5.19%
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = defaultdict(int)
        for c in s1:
            d[c] += 1
        bag = d.copy()
        taken = False
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            if c not in d:
                if taken:
                    bag = d.copy()
                l = r + 1
            else:
                if c not in bag:
                    while s2[l] != c:
                        bag[s2[l]] += 1
                        l += 1
                    l += 1
                else:
                    bag[c] -= 1
                    if bag[c] == 0:
                        del bag[c]
                    if not bag:
                        return True
                    taken = True
        return False