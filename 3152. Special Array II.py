"""
39 ms runtime beats 77.78%
47.16 MB memory beats 30.36%
"""
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)

        n = len(nums)
        # prefix sum
        presum = [0] * n
        for i in range(1, n):
            special = (nums[i] & 1) ^ (nums[i - 1] & 1)
            presum[i] = presum[i - 1] + special

        ln = len(queries)
        res = [False] * ln
        for i in range(ln):
            st, nd = queries[i]
            if presum[nd] - presum[st] == nd - st:
                res[i] = True
        return res