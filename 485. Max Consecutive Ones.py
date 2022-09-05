'''
runtime beats 95.87%
memory usage beats 29.99%
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1                
            else:
                maxcount.append(count)
                count = 0
                
        maxcount.append(count)
        return max(maxcount)
                