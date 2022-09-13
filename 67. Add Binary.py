'''
Runtime: 60 ms, faster than 35.95% of Python3 online submissions
Memory Usage: 13.9 MB, less than 73.02% of Python3 online submissions
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b1 = int(a, 2)
        b2 = int(b, 2)
        return format(b1+b2, 'b')