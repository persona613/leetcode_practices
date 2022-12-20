"""
113 ms runtime beats 78.9%
14.3 MB memory beats 24.56%
"""
class Solution:
    # find the count of nums that smaller than t
    def findsm(self, nums, t):
        cnt = 0
        for n in nums:
            if n <= t:
                cnt += 1
            else:
                break
        return cnt
    
    def bs(self, nums, srlist, mp):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            cnt = (m+1)+self.findsm(srlist, nums[m])
            if cnt == mp:
                return nums[m]
            elif cnt > mp:
                r = m-1
            elif cnt < mp:
                l = m+1
        return None
    
    def findmp(self, nums1, nums2, mp):
        ans = None
        while ans == None:
                if self.bs(nums1, nums2, mp):
                    ans = self.bs(nums1, nums2, mp)
                else:
                    ans = self.bs(nums2, nums1, mp)
                mp += 1
        return ans

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # decide median's position : count of nums smaller than median inclusive
        n1 = len(nums1)
        n2 = len(nums2)
        # mp is second median, first = mp-1
        mp = (n1+n2)//2 + 1
        if (n1+n2)%2 == 1:
            return self.findmp(nums1, nums2, mp)            
        else:
            ans1 = self.findmp(nums1, nums2, mp)
            ans2 = self.findmp(nums1, nums2, mp-1)
            return (ans1+ans2)/2
        
        