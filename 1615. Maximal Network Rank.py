"""
281 ms runtime beats 62.36%
18.14 MB memory beats 93.64%
"""
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        cnt = [0] * n
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
            cnt[a] += 1
            cnt[b] += 1
            
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                t = cnt[i] + cnt[j]
                if i in g[j]:
                    t -= 1
                if t > ans:
                    ans = t
        return ans
        