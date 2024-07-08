'''
Runtime: 162 ms, faster than 87.62% of Python3 online submissions
Memory Usage: 22.80 MB, less than 5.16% of Python3 online submissions
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l + 1, r - 1)
        helper(0, len(s) - 1)