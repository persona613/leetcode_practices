"""
44 ms runtime beats 6.58%
16.43 MB memory beats 91.99%
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # from itertools import zip_longest
        v1 = [int(s) for s in version1.split(".")]
        v2 = [int(s) for s in version2.split(".")]
        for x, y in zip_longest(v1, v2, fillvalue = 0):
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0