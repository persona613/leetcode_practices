"""
94 ms runtime beats 85.38%
17.86 MB memory beats 10.72%
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        ans = inf
        for i in range(n):
            l = 0
            r = m - 1
            while l < r:
                mid = (l + r) // 2
                a = binaryMatrix.get(i, mid)
                if a >= 1:
                    r = mid
                else:
                    l = mid + 1
            a = binaryMatrix.get(i, l)
            if a == 1 and l < ans:
                ans = l
        return -1 if ans == inf else ans
