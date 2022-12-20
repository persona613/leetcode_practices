"""
Submission Result: Time Limit Exceeded 
Last executed input:
719testcase01.txt
"""

class Solution:
    # all pairs' distances smaller than d
    def findpair(self, hs, sd, nd):
        cnt = 0
        for i in range(sd, nd+1, 1):
            if hs[i] != 0:
                cnt += hs[i]
        return cnt
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # {distance : count}
        hs = defaultdict(int)
        n = len(nums)
        if n == 2:
            return abs(nums[0]-nums[1]) 
        i = 0
        for i in range(n-1):
            for j in range(i+1, n):
                d = abs(nums[i]-nums[j])
                hs[d] += 1
        
        # max distance
        dmin = min(hs.keys())
        dmax = max(hs.keys())
        # last pair = max distance
        if k == n*(n-1)/2:
            return dmax
        
        cnt = 0
        # distance space
        ld = dmin
        rd = dmax
        md = (ld+rd)//2
        cnt = self.findpair(hs, ld, md)
        while ld < rd:
            if cnt >= k:
                rd = md
                md = (ld+rd)//2
                cnt -= self.findpair(hs, md+1, rd)
            elif cnt < k:
                ld = md+1
                md = (ld+rd)//2
                cnt += self.findpair(hs, ld, md)
        return ld
            