"""
Time Limit Exceeded
87 / 99 testcases passed
submitted at Apr 29, 2024 17:24
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def calculate(start, end):
            if start > end:
                return 0
            mi = start
            for i in range(start, end + 1):
                if heights[i] < heights[mi]:
                    mi = i
            return max(
                heights[mi] * (end - start + 1),
                calculate(start, mi - 1),
                calculate(mi + 1, end)
            )
        
        return calculate(0, len(heights) - 1)