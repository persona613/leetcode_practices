"""
Runtime Error

Runtime Error Message:
IndexError: list index out of range
    if st == dic[stack[-1]]:
Line 12 in isValid (Solution.py)
    ret = Solution().isValid(param_1)
Line 38 in _driver (Solution.py)
    _driver()
Line 49 in <module> (Solution.py)
Last executed input:
"){"
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}
        
        if len(s) %2 != 0:
            return False
        for st in s:
            if st in ['(', '{', '[']:
                stack.append(st)
            else:
                if st == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        
        return False
