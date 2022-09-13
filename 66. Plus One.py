'''
Runtime: 58 ms, faster than 32.6% of Python3 online submissions
Memory Usage: 13.8 MB, less than 58.52% of Python3 online submissions
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(i) for i in digits])
        num = int(num) + 1
        return list(str(num))