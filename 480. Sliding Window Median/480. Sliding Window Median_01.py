"""
Time Limit Exceeded
42 / 43 testcases passed
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        mxq = []
        miq = []
        for i in range(k):
            heapq.heappush(mxq, -nums[i])
            heapq.heappush(miq, -heapq.heappop(mxq))
            if len(miq) > len(mxq):
                heapq.heappush(mxq, -heapq.heappop(miq))
        odd = True if k % 2 == 1 else False
        if odd:
            res = [-mxq[0]]
        else:
            res = [(-mxq[0] + miq[0]) / 2]

        for i in range(k, len(nums)):
            pre = nums[i - k]
            if pre <= -mxq[0]:
                idx = mxq.index(-pre)
                mxq[idx] = -nums[i]
                heapq.heapify(mxq)
                heapq.heappush(miq, -heapq.heappop(mxq))
                heapq.heappush(mxq, -heapq.heappop(miq))
            else:
                idx = miq.index(pre)
                miq[idx] = nums[i]
                heapq.heapify(miq)
                heapq.heappush(mxq, -heapq.heappop(miq))
                heapq.heappush(miq, -heapq.heappop(mxq))
            if odd:
                res.append(-mxq[0])
            else:
                res.append((-mxq[0] + miq[0]) / 2)
        return res