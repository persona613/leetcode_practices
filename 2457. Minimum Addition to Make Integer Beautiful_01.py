"""
Wrong Answer
78 / 92 testcases passed
Input
n =
19
target =
1

Use Testcase
Output
1
Expected
81
"""
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ds = [int(c) for c in str(n)[::-1]]
        dsm = sum(ds)
        if dsm <= target:
            return 0

        for i in range(len(ds)):
            dsm -= ds[i]
            if dsm <= target:
                break
        return 10 ** (i + 1) - (n % (10 ** ( i + 1)))