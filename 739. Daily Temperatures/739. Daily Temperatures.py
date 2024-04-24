"""
914 ms runtime beats 62.15%
31.07 MB memory beats 77.67%
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [None] * len(temperatures)
        # min-monostack
        stk = []
        for i in range(len(temperatures)):
            while stk and stk[-1][0] < temperatures[i]:
                pre = stk.pop()
                arr[pre[1]] = i - pre[1]
            stk.append((temperatures[i], i))
            
        while stk:
            pre = stk.pop()
            arr[pre[1]] = 0
        return arr
            