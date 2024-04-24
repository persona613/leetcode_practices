"""
116 ms runtime beats 21.84%
18.61 MB memory beats 16.57%
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # rm = right_max array, lm = left_max array
        rm = deque()
        x = 0
        for a in height[::-1]:
            if a <= x:
                rm.appendleft(x)
            else:
                rm.appendleft(0)
                x = a
        x = 0
        lm = list()
        for a in height:
            if a <= x:
                lm.append(x)
            else:
                lm.append(0)
                x = a
        res = 0
        for i in range(n):
            h = min(rm[i], lm[i])
            if h > 0:
                res += h - height[i]
        return res