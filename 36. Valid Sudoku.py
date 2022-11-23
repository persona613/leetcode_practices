'''
Runtime: 122 ms, faster than 80.44% of Python3 online submissions 
Memory Usage: 14.0 MB, less than 6.86% of Python3 online submissions
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rmaps = {f"{r}":set() for r in range(1,10,1)}
        cmaps = {f"{c}":set() for c in range(1,10,1)}
        # matrix numbers map
        mmaps = {}
        for m in range(0,3,1):
            mmaps[f"{m}0"] = set()
            mmaps[f"{m}1"] = set()
            mmaps[f"{m}2"] = set()
        for i in range(0,9,1):
            for j in range(0,9,1):
                if board[i][j] == ".":
                    continue
                
                # row numbers
                if board[i][j] in rmaps[str(i+1)]:
                    return False
                else:
                    rmaps[str(i+1)].add(board[i][j])
                
                # colume numbers
                if board[i][j] in cmaps[str(j+1)]:
                    return False
                else:
                    cmaps[str(j+1)].add(board[i][j])
                
                # matrix numbers
                if board[i][j] in mmaps[f"{i//3}{j//3}"]:
                    return False
                else:
                    mmaps[f"{i//3}{j//3}"].add(board[i][j])
        return True
                