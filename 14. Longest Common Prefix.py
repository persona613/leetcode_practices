'''
Runtime: 82 ms, faster than 6.9% of Python3 online submissions
Memory Usage: 14 MB, less than 11.83% of Python3 online submissions
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strmin = 200
        ans = ''
        for s in strs:
            if len(s) < strmin:
                strmin = len(s)
        for w in range(strmin):
            i = 1
            while i < len(strs):
                if strs[i][w] == strs[i-1][w]:
                    pass
                else:
                    return ans
                i += 1
            ans += strs[0][w]
        return ans
                    
