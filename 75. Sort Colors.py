"""
63 ms runtime beats 48.21%
14 MB memory beats 15.27%
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*(2+1)
        for n in nums:
            counts[n] += 1
            
        # starting indices
        sums = 0
        for i, c in enumerate(counts):
            counts[i] = sums
            sums += c
            
        # new list init
        new = [0]*len(nums)
        for n in nums:
            new[counts[n]] = n
            counts[n] += 1
            
        # rewrite nums
        for i in range(len(nums)):
            nums[i] = new[i]
        # print(nums)
        