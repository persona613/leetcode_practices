"""
27 ms runtime beats 99.02%
16.21 MB memory beats 33.05%
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = 0 # prefix sum
        ms = float("inf")
        for n in nums:
            ps += n
            if ps < ms:
                ms = ps
        return 1-ms if ms<1 else 1