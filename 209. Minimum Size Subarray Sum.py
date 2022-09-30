'''
Runtime: 624 ms, faster than 11.86% of Python3 online submissions 
Memory Usage: 27.1 MB, less than 87.73% of Python3 online submissions
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        tsum = 0
        n = len(nums)
        i = 0
        for j in range(n):
            tsum += nums[j]
            while tsum >= target:
                ans = min(ans, j-i+1)
                # print(tsum)
                tsum -= nums[i]
                # print('minus:', tsum)
                i += 1
        return ans if ans != float('inf') else 0
            
                    
