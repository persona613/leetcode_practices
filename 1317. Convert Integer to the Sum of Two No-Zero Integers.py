"""
37 ms Beats 75.60%
16.42 MB Beats 5.90%
"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if "0" not in str(i) and "0" not in str(n-i):
                return [i, n-i]