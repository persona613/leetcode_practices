"""
46 ms runtime beats 33.45%
16.80 MB memory beats 22.33%
"""
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        dst = set()
        mi = float("inf")
        mx = float("-inf")
        ln = len(arr)
        for a in arr:
            dst.add(a)
            mi = min(mi, a)
            mx = max(mx, a)
        if len(dst) == 1:
            return True
        if len(dst) != ln:
            return False
        d = (mx-mi)/(ln-1)
        for i in range(ln):
            a = mi + i*d
            if a not in dst:
                return False
        return True