"""
Wrong Answer
6 / 47 testcases passed
Input
rectangles =
[[4,7],[4,9],[8,5],[6,2],[6,4]]
points =
[[4,2],[5,6]]

Use Testcase
Output
[5,2]
Expected
[5,0]
"""
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        arrx = []
        arry = []
        for x, y in rectangles:
            arrx.append(x)
            arry.append(y)
        arrx.sort()
        arry.sort()
        
        res = []
        n = len(rectangles)
        for x, y in points:
            xi = bisect.bisect_left(arrx, x)
            yi = bisect.bisect_left(arry, y)
            res.append(min(n - xi, n - yi))
        return res
