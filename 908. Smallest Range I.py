"""
134 ms runtime beats 23.10%
17.7 MB memory beats 13.91%
"""
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        Nmax, Nmin = nums[-1], nums[0]
        if Nmax - k > Nmin + k:
            return (Nmax - k) - (Nmin + k)
        return 0