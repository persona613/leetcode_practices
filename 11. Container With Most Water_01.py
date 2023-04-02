"""
Time Limit Exceeded
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def findnext(i, d):
            # d = 1 or -1
            if d == 1:
                while i+d < len(height):
                    if height[i] < height[i+d]:
                        return i+d
                    i += d
            elif d == -1:
                while i+d > -1:
                    if height[i] < height[i+d]:
                        return i+d
                    i += d
        def container(l, r):
            nonlocal res
            if l == None or r == None:
                return
            if l >= r:
                return
            water = abs(l-r) * min(height[l], height[r])
            if water > res:
                res = water
            if height[l] < height[r]:
                l2 = findnext(l, 1)
                container(l2, r)
            elif height[l] > height[r]:
                r2 = findnext(r, -1)
                container(l, r2)
            else:
                l2 = findnext(l, 1)
                container(l2, r)
                r2 = findnext(r, -1)
                container(l, r2)        
        res = 0
        container(0, len(height)-1)
        return res