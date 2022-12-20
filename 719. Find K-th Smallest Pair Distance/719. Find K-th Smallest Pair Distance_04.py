"""
Submission Result: Time Limit Exceeded 
Last executed input:
719testcase02.txt ans:292051
"""

class Solution:

    # all pairs' distances smaller than d
    def findpair(self, dis, dslist, sd, nd):
        cnt = 0        
        for d in range(sd, nd+1):
            cnt += dis[dslist[d]]
        return cnt
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 2:
            return abs(nums[0]-nums[1]) 
        
        # hs {num : count}
        hs = defaultdict(int)
        for n in nums:
            hs[n] += 1
        
        # dis {distance : count}
        dis = defaultdict(int)
        hskeys = list(hs.keys())
        # only one elements, distance=0
        if len(hskeys) < 2:
            return 0
        i = 0        
        for i in range(0, len(hskeys)):
            # record distance = 0
            dis[0] += hs[hskeys[i]]*(hs[hskeys[i]]-1)/2
            if i < len(hskeys)-1:
                for j in range(i+1, len(hskeys)):
                    d = abs(hskeys[i]-hskeys[j])
                    dis[d] += hs[hskeys[i]]*hs[hskeys[j]]
        # max distance
        dmin = min(dis.keys())
        dmax = max(dis.keys())
        # last pair = max distance
        if k == n*(n-1)/2:
            return dmax
        
        cnt = 0
        # distance space
        dslist = sorted(dis.keys())
        ld = 0
        rd = len(dslist)-1
        md = (ld+rd)//2
        cnt = self.findpair(dis, dslist, ld, md)
        while ld < rd:
            if cnt >= k:
                rd = md
                md = (ld+rd)//2
                cnt -= self.findpair(dis, dslist, md+1, rd)
            elif cnt < k:
                ld = md+1
                md = (ld+rd)//2
                cnt += self.findpair(dis, dslist, ld, md)
        return dslist[ld]
            