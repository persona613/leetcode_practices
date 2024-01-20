"""
460 ms runtime beats 98.54%
19.15 MB memory beats 45.20%
"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0: return True
        pre = float("-inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                if i-pre-1 < k:
                    return False
                pre = i
        return True