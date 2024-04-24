"""
Runtime Error
20 / 43 testcases passed
KeyError: 197941363
    ~~~~~~~^^^^^^
    deleted[drop] -= 1
Line 9 in mxq_remove (Solution.py)
    mxq_remove(mxq, 1)
Line 68 in medianSlidingWindow (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().medianSlidingWindow(param_1, param_2)
Line 99 in _driver (Solution.py)
    _driver()
Line 110 in <module> (Solution.py)
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def mxq_remove(hq, tail):
            if not tail:
                drop = -heapq.heappop(hq)
            else:
                drop = -hq.pop()
            deleted[drop] -= 1
            if deleted[drop] == 0:
                del deleted[drop]
            
        def miq_remove(hq, tail):
            if not tail:                
                drop = heapq.heappop(hq)
            else:
                drop = hq.pop()
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
