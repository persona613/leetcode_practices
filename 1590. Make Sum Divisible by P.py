"""
411 ms runtime beats 30.57%
35.00 MB memory beats 31.95%
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm = sum(nums)
        if sm % p == 0: return 0

        # target remainder, find subarray's sum = tr + p * k
        tr = sm % p
        # curr_remainder_index map: {prefix_sum % p: right most index}
        rmap = {0: 0}
        n = len(nums)
        res = n
        psum = 0
        for i in range(1, n + 1):
            psum += nums[i - 1]
            curr_remainder = psum % p
            diff = (curr_remainder - tr + p) % p
            if diff in rmap:
                res = min(res, i - rmap[diff])

            # update index map of r
            rmap[curr_remainder] = i
        return res if res != n else -1
            