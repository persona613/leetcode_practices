"""
5077 ms runtime beats 74.16%
14 MB memory beats 46.2%
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def findnext(k, i, j):
            nonlocal sta, end
            for d in [1,-1]:
                if i+d < len(board) and i+d > -1:
                    if board[i+d][j] == word[k]:
                        if k == end:
                            return True
                        board[i+d][j] = "#"
                        if findnext(k+1, i+d, j):
                            return True
                        else:
                            board[i+d][j] = word[k]
                if j+d < len(board[0]) and j+d > -1:
                    if board[i][j+d] == word[k]:
                        if k == end:
                            return True
                        board[i][j+d] = "#"
                        if findnext(k+1, i, j+d):
                            return True
                        else:
                            board[i][j+d] = word[k]
            return False                

        sta = 0
        end = len(word)-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if sta == end:
                        return True
                    board[i][j] = "#"
                    if findnext(sta+1,i,j):
                        return True
                    else:
                        board[i][j] = word[0]
        return False