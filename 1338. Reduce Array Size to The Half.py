"""
437 ms runtime beats 58.95%
38.49 MB memory beats 39.94%
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = dict()
        for a in arr:
            d[a] = d.get(a, 0) + 1
        feq = sorted(d.items(), key = lambda x: x[1], reverse = True)
        i = cnt = 0
        t = len(arr) / 2
        while cnt < t:
            cnt += feq[i][1]
            i += 1
        return i
