"""
580 ms runtime beats 87.85%
29.52 MB memory beats 17.14%
"""   
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # counting sort
        mi = min(nums)
        mx = max(nums)
        freq = dict()
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        
        idx = 0
        for v in range(mi, mx + 1):
            while freq.get(v, 0) > 0:
                nums[idx] = v
                freq[v] -= 1
                idx += 1
        return nums     