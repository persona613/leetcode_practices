"""
67 ms runtime beats 95.60%
16.85 MB memory beats 43.00%
"""
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # ref 907
        n = len(nums)
        mxq = [] # decreasing
        mxsum = 0
        for i in range(n):
            while mxq and nums[mxq[-1]] <= nums[i]:
                j = mxq.pop()
                leftbound = mxq[-1] if mxq else -1
                mxsum += nums[j] * ((j - leftbound) * (i - j))
            mxq.append(i)
        while mxq:
            j = mxq.pop()
            leftbound = mxq[-1] if mxq else -1
            mxsum += nums[j] * ((j - leftbound) * (n - j))
        
        miq = [] # increasing
        misum = 0
        for i in range(n):
            while miq and nums[miq[-1]] >= nums[i]:
                j = miq.pop()
                leftbound = miq[-1] if miq else -1
                misum += nums[j] * ((j - leftbound) * (i - j))
            miq.append(i)
        while miq:
            j = miq.pop()
            leftbound = miq[-1] if miq else -1
            misum += nums[j] * ((j - leftbound) * (n - j))
            
        return mxsum - misum
            


