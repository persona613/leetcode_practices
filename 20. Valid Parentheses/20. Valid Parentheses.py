"""
Runtime: 32 ms, faster than 93.53% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 26.43% of Python3 online submissions
"""

class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        cl = []
        dic = {'(':')', '{':'}', '[':']'}
        
        if len(s) %2 != 0:
            return False
        for st in s:
            if st in dic.keys():
                op.append(st)
                continue    
            if len(op) != 0:
                if st == dic[op[-1]]:
                    op.pop()
                    continue
            return False
        if len(op):
            return False
        return True
