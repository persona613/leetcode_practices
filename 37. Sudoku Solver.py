"""
116 ms runtime beats 90.54%
14 MB memory beats 73.58%
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        def scan():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        rowmap[i].add(board[i][j])
                        colmap[j].add(board[i][j])
                        groupmap[3*(i//3)+(j//3)].add(board[i][j])
                    else:
                        blank.append([i, j]) 
                        
        def check(i, j):
            # possible nums
            ret = []            
            for p in digits:
                if p in rowmap[i]:
                    continue
                if p in colmap[j]:
                    continue
                if p in groupmap[3*(i//3)+(j//3)]:
                    continue
                ret.append(p)
            return ret
        
        def write(i, j, p):
            board[i][j] = p
            rowmap[i].add(p)
            colmap[j].add(p)
            groupmap[3*(i//3)+(j//3)].add(p)
        
        def remove(i, j, p):
            board[i][j] = "."
            rowmap[i].remove(p)
            colmap[j].remove(p)
            groupmap[3*(i//3)+(j//3)].remove(p)            
        
        def solve(k):
            if k == len(blank):
                return True
            i, j = blank[k][0], blank[k][1]
            nums = check(i, j)
            if not nums:
                return False
            for n in nums:
                write(i, j, n)
                if solve(k+1):
                    return True
                else:
                    remove(i, j, n)
                        
        rowmap = {i:set() for i in range(9)}
        colmap = {j:set() for j in range(9)}
        groupmap = {g:set() for g in range(9)}
        digits = [str(d) for d in range(1, 10)]
        blank = []
        scan()
        solve(0)