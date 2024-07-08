"""
59 ms runtime beats 76.70%
23.24 MB memory beats 48.02%
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]

        ans = [0, 1]
        # add ans'count each time
        k = 2
        while k << 1 < n + 1:
            for i in range(k):
                ans.append(ans[i]+1)
            k <<= 1
        for i in range((n + 1) - k):
            ans.append(ans[i]+1)
        return ans