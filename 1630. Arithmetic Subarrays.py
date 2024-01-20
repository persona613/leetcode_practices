"""
161 ms runtime beats 78.40%
16.65 MB memory beats 14.03%
"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(nums, i, j):
            arr = sorted(nums[i: j+1])
            d = arr[1] - arr[0]
            for k in range(2, len(arr)):
                if arr[k] - arr[k-1] != d:
                    return False
            return True

        res = []
        for p in range(len(l)):
            res.append(check(nums, l[p], r[p]))
        return res