"""
22.6 ms runtime beats 46.15%
22.95 MB memory beats 46.15%
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def count_miss(idx):
            allnums = nums[idx] - nums[0] + 1
            return allnums - (idx + 1)

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            cnt = count_miss(mid)
            if cnt >= k:
                r = mid - 1
            else:
                l = mid + 1
        base = nums[r]
        return base + (k - count_miss(r))