"""
359 ms runtime beats 44.54%
22.01 MB memory beats 23.53%
"""
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        stk = [(nums[0], 0)]
        for i in range(1, n):
            a = nums[i]
            while stk and stk[-1][0] > a:
                _, j = stk.pop()
                ans += i - j
            stk.append((a, i))
        for a, i in stk:
            ans += (n - i)
        return ans