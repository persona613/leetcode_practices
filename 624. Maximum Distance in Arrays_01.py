"""
1463 ms runtime beats 89.70%
41.34 MB memory beats 66.40%
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mx1 = mx2 = (-inf, 0)
        mi1 = mi2 = (inf, 0)
        for i in range(len(arrays)):
            r = arrays[i][-1]
            l = arrays[i][0]
            if r > mx1[0]:
                mx2 = mx1
                mx1 = (r, i)
            elif r > mx2[0]:
                mx2 = (r, i)
            if l < mi1[0]:
                mi2 = mi1
                mi1 = (l, i)
            elif l < mi2[0]:
                mi2 = (l, i)
        
        if mx1[1] != mi1[1]:
            return abs(mx1[0]-mi1[0])
        return max(abs(mx1[0]-mi2[0]), abs(mx2[0]-mi1[0]))
