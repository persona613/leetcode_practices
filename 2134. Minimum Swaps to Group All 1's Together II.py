"""
618 ms runtime beats 99.55%
20.62 MB memory beats 37.84%
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # sliding window size
        size = nums.count(1)
        if size == 0 or size == 1 or size == len(nums):
            return 0

        # init circular array
        arr = nums.copy() + nums[:size]
        holes = 0
        for i in range(size):
            if arr[i] == 0:
                holes += 1
        ans = holes

        for i in range(size, len(arr)):
            if arr[i] == 0:
                holes += 1
            if arr[i - size] == 0:
                holes -= 1
            if holes < ans:
                ans = holes
        return ans