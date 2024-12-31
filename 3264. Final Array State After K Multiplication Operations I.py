"""
4 ms runtime beats 26.48%
17.30 MB memory beats 28.27%
"""
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [[v, i] for i, v in enumerate(nums)]
        heapq.heapify(arr)
        for _ in range(k):
            pair = heapq.heappop(arr)
            pair[0] *= multiplier
            heapq.heappush(arr, pair)
        res = [0] * len(arr)
        for v, i in arr:
            res[i] = v
        return res