'''
Runtime: 240 ms, faster than 45.37% of Python3 online submissions 
Memory Usage: 18.7 MB, less than 71.50% of Python3 online submissions
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        l = sorted(hm.items(), key=lambda x : x[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res