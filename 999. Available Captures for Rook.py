"""
43 ms runtime beats 73.35%
16.2 MB memory beats 83.11%
"""
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        # R position = [i, j]
        for i in range(n):
            try:
                j = board[i].index("R")
                break
            except ValueError:
                pass

        ans = 0
        ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d1, d2 in ds:
            t1 = i + d1
            t2 = j + d2
            while -1<t1<n and -1<t2<n:
                a = board[t1][t2]
                if a != ".":
                    if a == "p":
                        ans += 1
                    break
                t1 += d1
                t2 += d2
        return ans
            
