"""
78 ms runtime beats 61.84%
13.9 MB memory beats 37.11%
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def safe(cell):
            if cell[1] in attzone.keys():
                return False
            for q in attzone.keys():
                if cell in attzone[q]:
                    return False
            return True
        
        def place(cell):
            i, j = cell[0], cell[1]
            attzone[j] = []
            d = 1
            while i+d < n:
                if j+d < n:
                    attzone[j].append((i+d, j+d))
                if j-d >= 0:
                    attzone[j].append((i+d, j-d))
                d += 1
        
        def remove(cell):
            del attzone[cell[1]]
        
        def qs(row, cnt):
            # nonlocal attzone            
            for col in range(n):
                cell = (row, col)
                if safe(cell):
                    place(cell)
                    if row+1 == n:
                        cnt += 1
                    else:
                        cnt = qs(row+1, cnt)
                    remove(cell)
            return cnt        
        
        attzone = {}
        return qs(0, 0)
            
        