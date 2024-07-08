"""
1758 ms runtime beats 73.19%
17.07 MB memory beats 13.49%
"""
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def backtrack(i):
            if i == n:
                return 1

            curr = arr[i]
            ts = 0
            # take curr
            if curr - k < 0 or cnt[curr - k] == 0:
                cnt[curr] += 1
                ts += backtrack(i + 1)
                cnt[curr] -= 1

            # not take curr
            ts += backtrack(i + 1)
            return ts

        n = len(nums)
        cnt = [0] * 1001
        arr = sorted(nums)
        # minus 1 for empty subset
        return backtrack(0) - 1