"""
41 ms runtime beats 83.22%
14 MB memory beats 56.37%
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def pick(i):
            for d in nums:
                if d not in perm:
                    perm[i] = d
                    if i+1 == len(nums):
                        res.append(perm[:])
                    else:
                        pick(i+1)
                    perm[i] = None
        
        
        res = []
        perm = [None]*len(nums)
        pick(0)
        return res