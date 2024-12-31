"""
266 ms runtime beats 30.97%
36.26 MB memory beats 80.53%
"""
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # acc sum before i-th num(1-index)
        acc = [0]
        for v in nums:
            acc.append(v + acc[-1])

        # heapq: (sum of sub-array, end at i)
        q = []
        for i, v in enumerate(nums):
            heappush(q, (v, i))
        # sub-arrays sorted
        arr = []
        mod = 10 ** 9 + 7
        while len(arr) < right:
            sm, i = heappop(q)
            arr.append(sm)
            # add sub-array of one more element(end at i+1)
            if i < n - 1:
                heappush(q, (sm + nums[i + 1], i + 1))
        ans = 0
        for i in range(left - 1, right):
            ans = (ans + arr[i]) % mod
        return ans