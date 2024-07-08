"""
67.4 ms runtime beats 47.23%
31.88 MB memory beats 51.52%
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rm = [None] * n # right_min array
        stk = []
        for i in range(n):
            while stk and heights[stk[-1]] > heights[i]:
                pre = stk.pop()
                rm[pre] = i
            stk.append(i)
        while stk:
            pre = stk.pop()
            rm[pre] = n
        
        lm = [None] * n # left_min array
        for i in range(n-1, -1, -1):
            while stk and heights[stk[-1]] > heights[i]:
                pre = stk.pop()
                lm[pre] = i
            stk.append(i)
        while stk:
            pre = stk.pop()
            lm[pre] = -1

        ans = 0
        for i in range(n):
            area = heights[i] * (rm[i] - lm[i] - 1)
            if area > ans:
                ans = area
        return ans