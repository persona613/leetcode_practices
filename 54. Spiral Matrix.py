'''
Runtime: 42 ms, faster than 68.75% of Python3 online submissions
Memory Usage: 13.9 MB, less than 0% of Python3 online submissions
'''

'''test cases
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[1,2,3,4,5,6,7,8,9,10]]
[[1],[2],[3],[4],[5],[6]]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rmax = m
        rmin = 0
        cmax = n
        cmin = -1
        ans = []
        r, c = 0, 0
        while len(ans) < m*n:
            # move right
            while c < cmax:
                ans.append(matrix[r][c])
                c += 1
            if len(ans) == m*n:
                break
            cmax -= 1
            r += 1
            c -= 1  
            
            # move down
            while r < rmax:
                ans.append(matrix[r][c])
                r += 1
            if len(ans) == m*n:
                break
            rmax -= 1
            r -= 1
            c -= 1
            
            # move left
            while c > cmin:
                ans.append(matrix[r][c])
                c -= 1
            if len(ans) == m*n:
                break
            cmin += 1
            r -= 1
            c += 1
            
            # move up
            while r > rmin:
                ans.append(matrix[r][c])
                r -= 1
            if len(ans) == m*n:
                break
            rmin += 1
            r += 1
            c += 1
        return ans