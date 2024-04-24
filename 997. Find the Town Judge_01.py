"""
675 ms runtime beats 85.6%
22.1 MB memory beats 41.14%
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return n
        if not trust: return -1
        mt = dict() # map of trust count
        seen = set()
        for ts in trust:
            mt[ts[1]] = mt.get(ts[1], 0) + 1
            seen.add(ts[0])
        for k, v in mt.items():
            if v == n-1 and k not in seen:
                return k
        return -1

