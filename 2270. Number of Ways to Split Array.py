"""
741 ms runtime beats 94.03%
31.68 MB memory beats 48.67%
"""
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = [nums[0]]
        for v in nums[1:]:
            pre.append(v + pre[-1])
        tsum = pre[-1]
        ans = 0
        for i in range(len(nums)-1):
            lsum = pre[i]
            if lsum >= tsum - lsum:
                ans += 1
        return ans