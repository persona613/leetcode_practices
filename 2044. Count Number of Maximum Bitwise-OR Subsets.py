"""
23.8 ms runtime beats 77.92%
16.63 MB memory beats 45.24%
"""
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # choice or not choice
        # path = bitwise OR of curr set
        def backtrack(i, path):
            nonlocal ans
            if i == n:
                return

            # not take curr element
            backtrack(i + 1, path)

            # take curr element
            if path | nums[i] == mx:
                ans += 1
            backtrack(i + 1, path | nums[i])

        mx = 0
        for v in nums:
            mx |= v
        ans = 0
        n = len(nums)
        backtrack(0, 0)
        return ans