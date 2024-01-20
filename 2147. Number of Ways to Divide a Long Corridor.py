"""
377 ms runtime beats 75.71%
21.28 MB memory beats 21.43%
"""        
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # seat index
        sd = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                sd.append(i)
        sm = len(sd)
        if sm < 2 or sm % 2 == 1:
            return 0
        ans = 1
        mod = 10**9 + 7
        for i in range(1, len(sd)-1, 2):
            ans = (ans * (sd[i+1] - sd[i])) % mod
        return ans