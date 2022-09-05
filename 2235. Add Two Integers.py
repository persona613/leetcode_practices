'''
Runtime: 53 ms, faster than 34.37% of Python3 online submissions for Add Two Integers.
Memory Usage: 13.9 MB, less than 8.61% of Python3 online submissions for Add Two Integers.
'''
# python3
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2
        
'''
runtime beats 86.51%
memory usage beats 83.12%
'''
# python
class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2

# local test
input = [12, 5]

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


print(Solution().sum(*input))

