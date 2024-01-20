"""
Wrong Answer
31 / 100 testcases passed
Input
nums = [6,-1,9]
Use Testcase
Output 1
Expected 0
"""
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = [nums[0]]
        for v in nums:
            pre.append(v + pre[-1])
        tsum = pre[-1]
        ans = 0
        for i in range(len(nums)-1):
            lsum = pre[i]
            if lsum >= tsum - lsum:
                ans += 1
        return ans