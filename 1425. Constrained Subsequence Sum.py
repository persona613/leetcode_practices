"""
2548 ms runtime beats 5.18%
45.9 MB memory beats 5.60%
"""
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [None]*n
        maxheap = [pair(-inf, inf)]
        for i in range(n):
            idx = maxheap[0].idx
            val = maxheap[0].val
            while idx < i-k:
                heapq.heappop(maxheap)
                idx = maxheap[0].idx
                val = maxheap[0].val
            # dp[i] = nums[i] + max(dp[i-k]...dp[i-1],0)
            dp[i] = nums[i] + max(val, 0)
            heapq.heappush(maxheap, pair(dp[i], i))
            # print(dp)
        return max(dp)

class pair:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
    def __lt__(self, other):
        return self.val > other.val
    def __repr__(self):
        return f"({self.val}, {self.idx})"