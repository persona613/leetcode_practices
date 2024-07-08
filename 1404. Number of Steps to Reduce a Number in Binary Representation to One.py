"""
40 ms runtime beats 31.58%
16.30 MB memory beats 99.40%
"""
class Solution:
    def numSteps(self, s: str) -> int:
        ds = deque(s)
        ans = 0
        while len(ds) > 1:
            if ds[-1] == "0":
                ds.pop()
            else:
                i = len(ds) - 1
                while i >= 0 and ds[i] == "1":
                    ds[i] = "0"
                    i -= 1
                if i < 0:
                    ds.appendleft("1")
                else:
                    ds[i] = "1"
            ans += 1
        return ans