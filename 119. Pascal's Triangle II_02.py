'''
Runtime: 39 ms, faster than 67.86% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 16.29% of Python3 online submissions 
'''
class Solution:
    def __init__(self):
        # {i:[j0,j1,j2...]} => record pascal(i,j)
        self.dict = {i:[0]*(i+1) for i in range(34)}
        
    def pascal(self, i, j):
        if j==0 or j==i:
            return 1
        
        # if dict[i][j] = 0
        if not self.dict[i-1][j-1]:
            self.dict[i-1][j-1] = self.pascal(i-1, j-1)
        if not self.dict[i-1][j]:
            self.dict[i-1][j] = self.pascal(i-1, j)
            
        return self.dict[i-1][j-1] + self.dict[i-1][j]
    
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0]*(rowIndex+1)
        
        # elements' number = rowIndex
        # mid = rowIndex//2 + 1 -> mirror half list
        k = rowIndex
        for j in range(rowIndex//2 + 1):
            ans[j] = self.pascal(rowIndex, j)
            ans[k] = ans[j]
            k -= 1
        return ans
        