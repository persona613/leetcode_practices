"""
561 ms runtime beats 95.13%
23.69 MB memory beats 42.15%
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # record odd-number index to get -k and -k-1 index
        oddpos = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2:
                oddpos.append(i)
            if len(oddpos) > k:
                ans += oddpos[-k] - oddpos[-k-1]
        return ans