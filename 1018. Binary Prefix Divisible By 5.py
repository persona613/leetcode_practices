"""
213 ms runtime beats 68.94%
17.5 MB memory beats 69.88%
"""
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [True]*len(nums)
        ts = 0
        for i, v in enumerate(nums):
            ts = ts*2 + v
            ans[i] = ts % 5 == 0
        return ans