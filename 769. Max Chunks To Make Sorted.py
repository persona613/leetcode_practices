"""
0 ms runtime beats 100.00%
17.76 MB memory beats 14.45%
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # prefix sum == math sum
        return sum(sum(arr[: i + 1]) == i * (i + 1) // 2 for i in range(len(arr)))