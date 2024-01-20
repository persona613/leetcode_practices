"""
119 ms runtime beats 39.70%
19.41 MB memory beats 12.99%
"""
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt = []
        for s in bank:
            t = s.count("1")
            if t:
                cnt.append(t)
        ans = 0
        for i in range(len(cnt) - 1):
            ans += cnt[i] * cnt[i + 1]
        return ans