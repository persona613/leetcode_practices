"""
55 ms runtime beats 38.67%
17.70 MB memory beats 54.47%
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s)
        q = []
        for k, v in d.items():
            heapq.heappush(q, (-v, k))
        res = []
        while q:
            nv, k = heapq.heappop(q)
            res.append(k * -nv)
        return "".join(res)