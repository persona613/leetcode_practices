"""
1265 ms runtime beats 21.80%
28.1 MB memory beats 61.39%
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == len(nums):
            return sum(nums) / k
        if k == 1:
            return max(nums)
        i, j, sm, ans = 0, 0, 0, float('-inf')
        for i in range(len(nums)):
            sm += nums[i]
            if i-j+1 == k:
                ans = max(ans, sm/k)
                sm -= nums[j]
                j += 1
        return ans
            