'''
Runtime: 90 ms, faster than 64.88% of Python3 online submissions 
Memory Usage: 20.91 MB, less than 43.88% of Python3 online submissions
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for st in strs:
            k = tuple(sorted(st))
            g[k].append(st)
        return g.values()