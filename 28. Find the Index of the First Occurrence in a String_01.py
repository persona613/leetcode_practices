'''
Runtime: 41 ms, faster than 70.83% of Python3 online submissions
Memory Usage: 14 MB, less than 0% of Python3 online submissions
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)
        return idx