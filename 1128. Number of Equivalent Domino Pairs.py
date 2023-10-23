"""
199 ms runtime beats 99.77%
26.1 MB memory beats 71.46%
"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter(map(tuple, dominoes))
        ans = 0
        seen = set()
        for k, v in cnt.items():
            if k not in seen:
                seen.add(k)
                if k[0] != k[1]:
                    seen.add(k[::-1])
                    v += cnt.get(k[::-1], 0)
                ans += v*(v-1)//2
        return ans