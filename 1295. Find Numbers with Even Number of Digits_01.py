'''
142ms, runtime beats 0% !!!!!!
memory usage beats 85.84%
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digit = 1
            while i >= 10:
                i /= 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count