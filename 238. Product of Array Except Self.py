"""
268 ms runtime beats 36.51%
21.2 MB memory beats 69.27%
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)
        lsum = 1
        rsum = 1
        for i in range(1, len(nums)):
            j = len(nums)-1-i
            lsum = lsum * nums[i-1]
            rsum = rsum * nums[j+1]
            if ans[i] != None:
                ans[i] = ans[i] * lsum
            else:
                ans[i] = lsum
            if ans[j] != None:
                ans[j] = ans[j] * rsum
            else:
                ans[j] = rsum
        return ans
