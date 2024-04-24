"""
Time Limit Exceeded
34 / 42 testcases passed
"""
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        nxt_hight_R = [None] * n
        stk = []
        for i in range(n):
            h = heights[i]
            while stk and heights[stk[-1]] < h:
                j = stk.pop()
                nxt_hight_R[j] = i
            stk.append(i)
        while stk:
            nxt_hight_R[stk.pop()] = n - 1

        nxt_hight_L = [None] * n
        stk = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            while stk and heights[stk[-1]] < h:
                j = stk.pop()
                nxt_hight_L[j] = i
            stk.append(i)
        while stk:
            nxt_hight_L[stk.pop()] = 0
        
        res = []
        for i in range(n):
            j = nxt_hight_R[i]
            k = j - i
            for t in range(i+1, j+1):
                if nxt_hight_L[t] > i:
                    k -= 1
            res.append(k)
        return res
