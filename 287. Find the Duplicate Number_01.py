"""
1005 ms runtime beats 68.70%
28.4 MB memory beats 29.15%
"""
class Solution:
    def bs(self, nums, key):
        if not len(nums):
            return 
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == key:
                return key
            elif nums[m] < key:
                l = m+1
            elif nums[m] > key:
                r = m-1
        
    def findDuplicate(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i in nums:
            dic[i%1000].sort()
            if not self.bs(dic[i%1000],i):
                dic[i%1000].append(i)
            else:
                return self.bs(dic[i%1000],i)
        
                   