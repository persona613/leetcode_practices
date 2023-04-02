"""
826 ms runtime beats 31.98%
85.2 MB memory beats 10.58%
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def findnext(l, r, d):
            # d = 1, move left index
            # d = -1, move right index
            if d == 1:
                while l+d < r:
                    if height[l] < height[l+d]:
                        return l+d
                    l += d
            elif d == -1:
                while r+d > l:
                    if height[r] < height[r+d]:
                        return r+d
                    r += d
        def container(l, r):
            nonlocal res
            if l == None or r == None:
                return
            water = abs(l-r) * min(height[l], height[r])
            if water > res:
                res = water
            if height[l] < height[r]:
                l2 = findnext(l, r, 1)
                container(l2, r)
            elif height[l] > height[r]:
                r2 = findnext(l, r, -1)
                container(l, r2)
            else:
                l2 = findnext(l, r, 1)
                r2 = findnext(l, r, -1)
                container(l2, r2)        
        res = 0
        container(0, len(height)-1)
        return res