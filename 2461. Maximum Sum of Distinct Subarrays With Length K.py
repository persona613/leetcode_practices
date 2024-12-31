"""
134 ms runtime beats 41.56%
36.37 MB memory beats 34.30%
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ws = ans = 0
        bag = defaultdict(int)
        for i in range(k):
            bag[nums[i]] += 1
            ws += nums[i]
        if len(bag) == k:
            ans = ws
        
        for i in range(k, len(nums)):
            bag[nums[i]] += 1
            ws += nums[i]
            
            bag[nums[i - k]] -= 1
            if bag[nums[i - k]] == 0:
                del bag[nums[i - k]]
            ws -= nums[i - k]

            if len(bag) == k:
                ans = max(ans, ws)
        return ans