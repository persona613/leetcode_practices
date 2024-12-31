"""
303 ms runtime beats 59.04%
18.91 MB memory beats 43.09%
"""
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = [0] * 26
        base = ord("a")
        for c in s:
            cnt[ord(c) - base] += 1

        q = []
        for i in range(26):
            if cnt[i] != 0:
                q.append(-i)
        heapq.heapify(q)

        res = []
        precode = None
        while q:
            if precode == -q[0]:
                if len(q) == 1:
                    break
                mxcode = -heapq.heappop(q)
                second_mxcode = -heapq.heappop(q)
                res.append(chr(second_mxcode + base))
                cnt[second_mxcode] -= 1
                if cnt[second_mxcode]:
                    heapq.heappush(q, -second_mxcode)
                heapq.heappush(q, -mxcode)
                precode = second_mxcode

            code = -heapq.heappop(q)
            take = min(cnt[code], repeatLimit)
            res.append(chr(code + base) * take)
            cnt[code] -= take
            if cnt[code]:
                heapq.heappush(q, -code)
            precode = code
        return "".join(res)