"""
861 ms runtime beats 100%
30.81 MB memory beats 5.75%
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = tm = ans = 0
        d = dict()
        for r in range(len(nums)):
            v = nums[r]
            if v in d:
                del_idx = d[v]
                while l <= del_idx:
                    del d[nums[l]]
                    tm -= nums[l]
                    l += 1
            d[v] = r
            tm += v
            ans = max(ans, tm)
        return ans