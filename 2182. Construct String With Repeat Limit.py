"""
149 ms runtime beats 94.93%
19.80 MB memory beats 8.74%
"""
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        stk = sorted(Counter(s).items())
        res = []
        while stk:
            char, cnt = stk.pop()
            use = min(cnt, repeatLimit)
            res.append(char * use)
            if cnt > use and stk:
                nxt_char, nxt_cnt = stk.pop()
                res.append(nxt_char)
                if nxt_cnt > 1:
                    stk.append((nxt_char, nxt_cnt - 1))

                stk.append((char, cnt - use))
        return "".join(res)