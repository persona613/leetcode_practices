"""
26 ms runtime beats 95.29%
16.70 MB memory beats 9.42%
"""
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ds = [int(c) for c in str(n)[::-1]]
        dsm = sum(ds)
        if dsm <= target:
            return 0

        for i in range(len(ds)):
            dsm -= ds[i]
            if dsm < target:
                break
        return 10 ** (i + 1) - (n % (10 ** ( i + 1)))