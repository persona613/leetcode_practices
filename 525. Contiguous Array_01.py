"""
712 ms runtime beats 27.99%
21.76 MB memory beats 29.90%
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        d[0] = -1
        curr = ans = 0
        for i in range(len(nums)):
            curr += 1 if nums[i]==1 else -1
            if curr in d:
                ans = max(ans, i-d[curr])
            else:
                d[curr] = i
        return ans