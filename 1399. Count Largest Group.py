"""
95 ms runtime beats 50.10%
16.2 MB memory beats 67.88%
"""
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # dc={sum of digis: count}
        dc = defaultdict(int)
        for i in range(1, n+1):
            sm = sum(int(c) for c in str(i))
            dc[sm] += 1
        cns = sorted(dc.values(), reverse=True)
        k = cns[0]
        return cns.count(k)