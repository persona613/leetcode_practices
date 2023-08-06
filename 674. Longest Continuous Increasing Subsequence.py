"""
87 ms runtime beats 59.89%
17.8 MB memory beats 50.80%
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        cnt = 1
        pre = nums[0]
        for n in nums:
            if n > pre:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            pre = n
        return max(ans, cnt)