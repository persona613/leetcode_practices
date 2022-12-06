"""
Runtime: 3643 ms, faster than 21.87% of Python3 online submissions 
Memory Usage: 28.5 MB, less than 46.07% of Python3 online submissions
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk = []
        
        for i, t in enumerate(temperatures):
            
            while stk and t > temperatures[stk[-1]]:
                res[stk[-1]] = i-stk[-1]
                stk.pop()
            
            stk.append(i)
            
        return res
            