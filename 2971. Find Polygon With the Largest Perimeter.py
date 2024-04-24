"""
509 ms runtime beats 81.34%
31.42 MB memory beats 97.22%
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        n = len(arr)
        presum = [arr[0]]
        for i in range(1, n):
            presum.append(arr[i] + presum[i - 1])

        for i in range(n-1, 1, -1):
            if presum[i - 1] > arr[i]:
                return presum[i - 1] + arr[i]
        return -1
