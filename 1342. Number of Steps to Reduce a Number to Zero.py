
'''
Runtime: 42 ms, faster than 68.15% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 14 MB, less than 8.27% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num %2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count