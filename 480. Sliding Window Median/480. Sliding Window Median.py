"""
290 ms runtime beats 58.15%
31.25 MB memory beats 18.21%
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def mxq_remove(hq, tail):
            if not tail:
                drop = -heapq.heappop(hq)
            else:
                stk = []
                while hq and -hq[-1] not in deleted:
                    stk.append(-hq.pop())
                drop = -hq.pop()

                while stk:
                    heapq.heappush(hq, -stk.pop())

            deleted[drop] -= 1
            if deleted[drop] == 0:
                del deleted[drop]
            
        def miq_remove(hq, tail):
            if not tail:                
                drop = heapq.heappop(hq)
            else:
                stk = []
                while hq and hq[-1] not in deleted:
                    stk.append(hq.pop())
                drop = hq.pop()

                while stk:
                    heapq.heappush(hq, stk.pop())

            deleted[drop] -= 1
            if deleted[drop] == 0:
                del deleted[drop]

        mxq = []
        miq = []
        deleted = dict()
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
            # element out of window
            pre = nums[i - k]
            # lazy remove: mark deleted
            deleted[pre] = deleted.get(pre, 0) + 1
            # balance two heap by push inf or -inf
            if pre <= -mxq[0]:
                heapq.heappush(miq, inf)
                deleted[inf] = deleted.get(inf, 0) + 1
            else:
                heapq.heappush(mxq, inf)
                deleted[-inf] = deleted.get(-inf, 0) + 1

            # insert new element
            heapq.heappush(mxq, -nums[i])
            heapq.heappush(miq, -heapq.heappop(mxq))
            while len(miq) > len(mxq):
                heapq.heappush(mxq, -heapq.heappop(miq))

            # clear two heap
            while mxq and -mxq[0] in deleted:
                mxq_remove(mxq, 0)
                # balance two heap
                if miq and miq[0] in deleted:
                    miq_remove(miq, 0)
                else:
                    miq_remove(miq, 1)
            while miq and miq[0] in deleted:
                miq_remove(miq, 0)
                if mxq and -mxq[0] in deleted:
                    mxq_remove(mxq, 0)
                else:
                    mxq_remove(mxq, 1)

            if odd:
                res.append(-mxq[0])
            else:
                res.append((-mxq[0] + miq[0]) / 2)
        return res
