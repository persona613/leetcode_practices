'''
Runtime: 186 ms, faster than 70.69% of Python3 online submissions 
Memory Usage: 17.1 MB, less than 96.07% of Python3 online submissions
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for st in strs:
            sor = "".join(sorted(st))
            if sor in ans:
                ans[sor].append(st)
            else:
                ans[sor] = [st]
        return list(ans.values())