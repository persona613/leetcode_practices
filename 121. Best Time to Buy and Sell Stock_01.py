"""
2348 ms runtime beats 24.85%
23.1 MB memory beats 99.79%
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def divide(i, nums):
            nonlocal maxprofit, leftmin, rightmax
            if len(nums) == 1:
                if nums[0] < leftmin[1]:
                    leftmin = [i, nums[0]]
                    if leftmin[0] > rightmax[0]:
                        rightmax = [0, float("-inf")]
                if nums[0] > rightmax[1] and i > leftmin[0]:
                    rightmax = [i, nums[0]]
                if rightmax[1] - leftmin[1] > maxprofit:
                    maxprofit = rightmax[1] - leftmin[1]
                return               
            m = len(nums)//2
            divide(i, nums[:m])
            divide(i+m, nums[m:])
        
        # leftmin = [index, price], rightmax = [index, price]
        leftmin = [0, float("inf")]
        rightmax = [0, float("-inf")]
        maxprofit = 0
        divide(0, prices)
        return maxprofit