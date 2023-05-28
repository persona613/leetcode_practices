"""
43 ms runtime beats 39.6%
16.3 MB memory beats 6.59%
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        ca, cl = 0, 0 # count absent, late
        for c in s:
            if c == "A":
                ca += 1
                if ca == 2:
                    return False
                cl = 0
            elif c == "L":
                cl += 1
                if cl == 3:
                    return False
            else:
                cl = 0
                continue
        return True