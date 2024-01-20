"""
35 ms runtime beats 89.02%
16.26 MB memory beats 64.03%
"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = Counter(s)
        n = d[s[0]]
        for k in d:
            if d[k] != n:
                return False
        return True
        # return len(set(d.values())) == 1