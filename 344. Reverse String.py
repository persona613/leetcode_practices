'''
Runtime: 214 ms, faster than 73.36% of Python3 online submissions
Memory Usage: 43.2 MB, less than 5% of Python3 online submissions
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(lo, hi):
            if lo >= hi:
                return
            helper(lo+1, hi-1)
            s[lo], s[hi] = s[hi], s[lo]            
        
        helper(0, len(s)-1)