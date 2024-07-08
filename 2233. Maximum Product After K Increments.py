"""
1113 ms runtime beats 20.33%
27.42 MB memory beats 18.13%
"""
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # modulo product/sum at every step is ok
        arr = nums[:]
        heapq.heapify(arr)
        step = 0
        while step < k:
            mi = heapq.heappop(arr)
            heapq.heappush(arr, mi + 1)
            step += 1
            
        ans = 1
        MOD = 10**9 + 7
        while arr:
            ans = ans * heapq.heappop(arr) % MOD
        return ans