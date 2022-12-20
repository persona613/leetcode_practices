"""
49 ms runtime beats 64.54%
13.9 MB memory beats 64.16%
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mi = (l+r) // 2
            if not isBadVersion(mi):
                l = mi + 1
            else:
                r = mi
        if isBadVersion(l-1) == False and isBadVersion(l) == True:
            return l
        
        
        