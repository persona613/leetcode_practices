"""
35 ms runtime beats 65.05%
16.67 MB memory beats 21.40%
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if abs(m - n) > 1 or s == t:
            return False

        i = j = dis = 0
        while i < m and j < n:
            if s[i] != t[j]:
                if dis > 0:
                    return False
                else:
                    if m == n:
                        i += 1
                        j += 1
                    elif m > n:
                        i += 1
                    else:
                        j += 1
                    dis += 1
            else:
                i += 1
                j += 1
        return True