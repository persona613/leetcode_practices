"""
65 ms runtime beats 72.97%
16.3 MB memory beats 87.93%
"""
class Solution:
    def sortString(self, s: str) -> str:
        dc = Counter(s)
        res, w = [], 0
        while dc:
            ks = sorted(dc.keys(),reverse=w)
            for k in ks:
                res.append(k)
                if dc[k] > 1:
                    dc[k] -= 1
                else:
                    del dc[k]
            w ^= 1
        return "".join(res)            



        # dc = Counter(s)
        # res, w = [], 0
        # while dc:
        #     ks = sorted(dc.keys())
        #     mk, ct = dc.most_common()[-1]
        #     qt = ct // 2
        #     # w=1,next string: backward, ks[::-1]
        #     # w=0,next string: forward, ks
        #     if qt:
        #         if w:
        #             ksd = ks[::-1] + ks
        #         else:
        #             ksd = ks + ks[::-1]
        #     for _ in range(qt):
        #         res.extend(ksd)
        #     r = ct % 2
        #     if r:
        #         if w:
        #             res.extend(ks[::-1])
        #         else:
        #             res.extend(ks)
        #     for k in ks:
        #         dc[k] -= ct
        #         if dc[k] ==0:
        #             del dc[k]
        #     # w = (w+r)%2
        #     w ^= r
        # return "".join(res)