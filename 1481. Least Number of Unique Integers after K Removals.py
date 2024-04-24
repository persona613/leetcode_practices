"""
332 ms runtime beats 74.71%
36.86 MB memory beats 40.07%
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == 0: return len(set(arr))
        f = Counter(arr)
        n = len(f)
        ar = sorted(f.items(), key = lambda x: x[1])
        acc = 0
        for i in range(n):
            acc += ar[i][1]
            if acc > k:
                break
        else:
            return 0
        return n - i