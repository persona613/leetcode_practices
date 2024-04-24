"""
Wrong Answer
20 / 98 testcases passed
Editorial
Input
nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19

Use Testcase
Output 24
Expected 18
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        ans = l = 0
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            if cur >= k:
                cur //= nums[l]
                l += 1
            ans += i - l + 1
        return ans