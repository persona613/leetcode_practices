"""
215 ms runtime beats 98.03%
17.5 MB memory beats 61.71%
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        dq = deque(num)
        i = -1 # inverse index
        ad = 0 # carry number
        while k > 0 or ad == 1:
            r = k % 10
            if i >= -len(dq):
                if dq[i] + r + ad >= 10:
                    dq[i] = dq[i] + r + ad - 10
                    ad = 1
                else:
                    dq[i] = dq[i] + r + ad
                    ad = 0
            else:
                if r + ad >= 10:
                    dq.appendleft(r + ad - 10)
                    ad = 1
                else:
                    dq.appendleft(r + ad)
                    ad = 0
            k = k // 10
            i -= 1
        return dq
            
        # --- conbine in first while ---
        # while ad:
        #     if i >= -len(dq):
        #         if dq[i] + ad >= 10:
        #             dq[i] = dq[i] + ad - 10
        #             ad = 1
        #         else:
        #             dq[i] = dq[i] + ad
        #             ad = 0
        #     else:
        #         dq.appendleft(ad)
        #         ad = 0
        # return dq