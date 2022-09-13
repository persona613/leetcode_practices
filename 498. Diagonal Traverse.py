'''
Runtime: 418 ms, faster than 15.2% of Python3 online submissions
Memory Usage: 17.1 MB, less than 78.81% of Python3 online submissions
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        r, c = 0, 0
        ans = []
        up = 1
        d = 0
        while d < m+n:
            if up == 1:
                while r > -1 and c < n:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                if c >= n:
                    r += 1
                    c -= 1
                    r += 1
                else:
                    r += 1
                up = 0
            else:
                while r < m and c > -1:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                if r >= m:
                    r -= 1
                    c += 1
                    c += 1
                else:
                    c += 1
                up =1
            d = r + c
        return ans
                    