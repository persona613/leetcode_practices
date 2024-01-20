"""
1050 ms runtime beats 24.15%
27.99 MB memory beats 56.73%
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        mav = cur / k
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            mav = max(mav, cur / k)
        return mav            
            
            