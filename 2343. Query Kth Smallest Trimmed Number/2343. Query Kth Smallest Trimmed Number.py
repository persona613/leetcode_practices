"""
359 ms runtime beats 99.53%
14.2 MB memory beats 46.95%
"""
class Solution:
    def countingsort(self, lst, t, d=10):
        counts = {i:[] for i in "0123456789"}
        for sr in lst:
            key = sr[0][t]
            counts[key].append(sr)
       
        # init new list for sort elements and elements' index
        elist = []
        for i in range(10):
            elist.extend(counts[str(i)])            
        return elist
        
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        trimap = defaultdict(list)
        maxd = len(nums[0])
        base = [ [n, i] for i, n in enumerate(nums)]
        
        for t in range(-1, -maxd-1, -1):
            tmp = self.countingsort(base, t)
            trimap[-t] = tmp
            base = tmp
                
        for k, trim in queries:
            res.append(trimap[trim][k-1][1])
            
        return res