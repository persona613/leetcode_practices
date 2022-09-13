'''
Runtime: 59 ms, faster than 21.16% of Python3 online submissions
Memory Usage: 13.7 MB, less than 97.18% of Python3 online submissions
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1