"""
52 ms runtime beats 36.13%
14.5 MB memory beats 5.35%
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search in first-col for row-index
        def bs_row(l, r):
            while l+1 < r:
                mid = (l+r) // 2
                if target < matrix[mid][0]:
                    r = mid
                else:
                    l = mid
            return l

        def bs_col(l, r):
            nonlocal i
            while l <= r:
                mid = (l+r) // 2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        i = bs_row(0, len(matrix))
        if i == target:
            return True
        return bs_col(0, len(matrix[0])-1) == True