"""
776 ms runtime beats 73.96%
31.26 MB memory beats 79.26%
"""
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        t = sum(nums) / 2
        arr = [-v for v in nums]
        heapq.heapify(arr)
        
        ans = 0
        while t > 0:
            a = heapq.heappop(arr) / 2
            t += a
            heapq.heappush(arr, a)
            ans += 1
        return ans