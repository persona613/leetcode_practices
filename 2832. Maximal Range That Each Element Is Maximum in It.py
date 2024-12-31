"""
274 ms runtime beats 30.87%
40.89 MB memory beats 42.77%
"""
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        # decreasing monotonic stack
        stk = []
        for i in range(n):
            curr = nums[i]
            while stk and stk[-1][0] < curr:
                _, pi = stk.pop()
                res[pi] += i - pi
            stk.append((curr, i))
        while stk:
            _, pi = stk.pop()
            res[pi] += n - pi

        # from right side
        for i in range(n - 1, -1, -1):
            curr = nums[i]
            while stk and stk[-1][0] < curr:
                _, pi = stk.pop()
                res[pi] += pi - i
            stk.append((curr, i))
        while stk:
            _, pi = stk.pop()
            res[pi] += pi + 1

        return res
        