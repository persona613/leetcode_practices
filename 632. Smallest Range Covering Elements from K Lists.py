"""
207 ms runtime beats 31.05%
23.93 MB memory beats 21.56%
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        miq = [(nums[i][0], i, 0) for i in range(m)]
        heapq.heapify(miq)
        mxq = [-nums[i][0] for i in range(m)]
        heapq.heapify(mxq)

        diff = inf
        while True:
            curr_mi, i, j = heapq.heappop(miq)
            curr_diff = -mxq[0] - curr_mi
            if curr_diff < diff:
                diff = curr_diff
                ans = [curr_mi, -mxq[0]]
            if j + 1 == len(nums[i]):
                break
            heapq.heappush(miq, (nums[i][j + 1], i, j + 1))
            heapq.heappush(mxq, -nums[i][j + 1])
        return ans