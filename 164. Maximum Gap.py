"""
2103 ms runtime beats 63.49%
28 MB memory beats 68.87%
"""
class Solution:
    def countingsort(self, nums: List[int], p: int, d=10) -> List[int]:
        counts = [0]*d
        for n in nums:
            key = (n // p) % 10
            counts[key] += 1
            
        # starting indeices
        start = 0
        for i, c in enumerate(counts):
            counts[i] = start
            start += c
            
        # init new list for sort
        new = [0]*len(nums)
        for n in nums:
            key = (n // p) % 10
            new[counts[key]] = n
            counts[key] += 1            
        return new
    
    def radixsort(self, nums: List[int]) -> List[int]:
        p = 1
        while p <= max(nums):
            nums = self.countingsort(nums, p)
            p *= 10        
        return nums
    
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        slist = self.radixsort(nums)
        maxd = float("-inf")
        
        for i in range(1, len(slist), 1):
            d = slist[i]-slist[i-1]
            if d > maxd:
                maxd = d
        return maxd
        