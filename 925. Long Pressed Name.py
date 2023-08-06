"""
38 ms runtime beats 96.93%
16.4 MB memory beats 46.79%
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        n = len(name)
        m = len(typed)
        while i < n:
            k = i
            t = j
            c = name[k]
            while i<n and name[i] == c:
                i += 1
            while j<m and typed[j] == c:
                j += 1
            if i-k > j-t:
                return False
        return j >= m