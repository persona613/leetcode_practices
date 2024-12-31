"""
604 ms runtime beats 5.01%
24.94 MB memory beats 23.40%
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # max stk, maintain decreasing, meet next big
        stk = []
        for i, v in enumerate(nums):
            while stk and stk[-1][0] <= v:
                stk.pop()
            stk.append((v, i))

        # stk[j][0] = max element in nums[i:]
        # binary search to find farest sub_peaks
        stk = stk[::-1]
        ans = 0
        for i, v in enumerate(nums):
            if v > stk[-1][0]:
                continue
            t = bisect_left(stk, v, key = lambda x: x[0])
            ans = max(ans, stk[t][1] - i)
        return ans