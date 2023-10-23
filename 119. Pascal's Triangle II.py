'''
Runtime: 37 ms, faster than 68.36% of Python3 online submissions 
Memory Usage: 16.2 MB, less than 82.18% of Python3 online submissions 
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1] + [0]*rowIndex
        cur = pre.copy()
        for i in range(1, rowIndex+1):
            for j in range(i+1):
                if j==0 or j==i:
                    cur[j] = 1
                else:
                    cur[j] = pre[j] + pre[j-1]
            pre, cur = cur, pre
        return pre
        