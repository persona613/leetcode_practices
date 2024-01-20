"""
778 ms runtime beats 18.79%
32.70 MB memory beats 6.69%
"""
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        suffix = []
        res = []
        prefix.append(nums[0])
        for a in nums[1:]:
            prefix.append(prefix[-1]+a)
        suffix.append(prefix[-1])
        for a in nums[:-1]:
            suffix.append(suffix[-1]-a)
        for i in range(n):
            a = nums[i]
            if i==0:
                v = suffix[i+1]-a*(n-1-i)
            elif i==n-1:
                v = a*i-prefix[i-1]
            else:
                v = a*i-prefix[i-1] + suffix[i+1]-a*(n-1-i)
            res.append(v)
        return res