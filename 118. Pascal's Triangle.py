'''
Runtime: 62 ms, faster than 14.16% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 0% of Python3 online submissions 
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        inter = []
        
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1,1])
            else:
                inter.append(1)
                for j in range(i+1-2):
                    val = ans[i-1][j]+ans[i-1][j+1]
                    inter.append(val)
                inter.append(1)
                ans.append(inter[:])
                inter.clear()
        return ans