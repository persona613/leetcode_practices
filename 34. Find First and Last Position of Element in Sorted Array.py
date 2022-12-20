"""
193 ms runtime beats 44.32%
15.5 MB memory beats 10.86%
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans
        # left boundary
        def findleft(nums, l, r, target):
            m = (l+r) // 2
            while l+1 < r:
                if nums[m] == target:
                    r = m
                elif nums[m] < target:
                    l = m
                m = (l+r) // 2
            return r
        # right boundary
        def findright(nums, l, r, target):
            m = (l+r) // 2
            while l+1 < r:
                if nums[m] == target:
                    l = m
                elif nums[m] > target:
                    r = m
                m = (l+r) // 2
            return l
        
        l = -1
        r = len(nums)
        m = (l+r) // 2
        while l+1 < r:
            if nums[m] == target:
                ans[0] = findleft(nums, l, m, target)
                ans[1] = findright(nums, m, r, target)
                return ans
            elif nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m
            m = (l+r) // 2
        return ans
            