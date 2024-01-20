"""
Submission Result: Wrong Answer 
Input:
[-4,-1,0,3,10]
Output:
[16,1,0,9,100]
Expected:
[0,1,9,16,100]
""" 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            a = nums[l]**2
            b = nums[r]**2
            if a <= b:
                res.append(a)
                l += 1
            else:
                res.append(b)
                r -= 1
        return res