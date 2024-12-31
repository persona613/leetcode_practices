"""
189 ms runtime beats 71.67%
31.82 MB memory beats 44.84%
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = len(nums) + 1
        # presum queue: [(presum index, presum value)]
        pq = deque([(-1, 0)])
        # curr presum
        curr = 0
        for i, v in enumerate(nums):
            curr += v
            # monotonic queque:
            # if presum[x] < curr, it is impossible to make k
            # and curr index provid better range for latter presum[y]
            while pq and pq[-1][1] >= curr:
                pq.pop()
            
            while pq and curr - pq[0][1] >= k:
                ps = pq.popleft()
                ans = min(ans, i - ps[0])
            pq.append((i, curr))
        return ans if ans < len(nums) + 1 else -1