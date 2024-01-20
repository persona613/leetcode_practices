"""
Time Limit Exceeded
52 / 56 testcases passed
"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        heads = []
        colmax = 1
        n = len(nums)
        for row in nums:
            if len(row) > colmax:
                colmax = len(row)
        for i in range(n):
            heads.append((i, 0))
        for j in range(1, colmax):
            heads.append((n-1, j))
        for i, j in heads:
            while i>=0 and j<colmax:
                try:
                    res.append(nums[i][j])
                    i -= 1
                    j += 1
                except IndexError:
                    i -= 1
                    j += 1
        return res
        