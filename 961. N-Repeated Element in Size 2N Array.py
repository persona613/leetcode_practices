"""
188 ms runtime beats 94.44%
17.8 MB memory beats 34.44%
"""
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            if n in m:
                return n
            m.add(n)