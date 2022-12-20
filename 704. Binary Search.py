'''
Runtime: 245 ms, faster than 96.3% of Python3 online submissions 
Memory Usage: 15.6 MB, less than 26.44% of Python3 online submissions
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        en = len(nums)
        mi = en // 2
        while st != mi:
            if target >= nums[mi]:
                st = mi
                mi = (st+en) // 2
            else:
                en = mi
                mi = (st+en) // 2
        if nums[mi] == target:
            return mi
        else:
            return -1
        