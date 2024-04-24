"""
708 ms runtime beats 93.43%
30.83 MB memory beats 91.77%
"""
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        arr = sorted(nums)
        res = []
        for i in range(0, len(nums), 3):
            if arr[i+2] - arr[i] <= k:
                res.append(arr[i:i+3])
            else:
                return []
        return res