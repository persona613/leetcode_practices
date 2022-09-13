'''
Runtime: 211 ms, faster than 67.5% of Python3 online submissions
Memory Usage: 15.3 MB, less than 0% of Python3 online submissions
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = []
        full = sum(nums)
        # print(full)
        
        if len(nums) == 1:
            return 0
        
        if 0 == full-nums[0]:
            ans.append(0)
        if full-nums[-1] == 0:
            ans.append(len(nums)-1)
        
        i = 1
        left = nums[0]
        right = full - nums[1] - nums[0]
        for i in range(1, len(nums)-1):
            # print(left, right)
            if left == right:
                ans.append(i)
            left = left + nums[i]
            right = right - nums[i+1]
            i += 1          
                
        if ans:
            return min(ans)
        
        return -1