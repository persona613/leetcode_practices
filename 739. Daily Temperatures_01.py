"""
Time Limit Exceeded
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
              
        for i, t in enumerate(temperatures):
            stk = [t]
            j = i+1
            find = False
            
            while j < len(temperatures):
                if temperatures[j] > stk[-1]:
                    ans.append(j-i)
                    find = True
                    break
                else:
                    stk.append(stk[-1])
                    j += 1
                    
            if find == False:
                ans.append(0)
        
        return ans