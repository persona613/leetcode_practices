'''
Runtime: 67 ms, faster than 9.3% of Python3 online submissions 
Memory Usage: 13.8 MB, less than 63.41% of Python3 online submissions 
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        uprow = [1,1]
        ans = []
        i = 2
        while i < rowIndex+1:
            ans.clear()
            ans.append(1)
            for j in range(i+1-2):
                # print(uprow)
                elem = uprow[j]+uprow[j+1]
                ans.append(elem)
            ans.append(1)
            uprow[:] = ans[:]
            # print(uprow)
            i += 1
        return ans