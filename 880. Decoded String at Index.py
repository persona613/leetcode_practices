"""
42 ms runtime beats 21.21%
16.1 MB memory beats 98.48%
"""
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stk = []
        sb = [] # sub-string
        tl = 0 # tape length
        for ch in s:
            if ch.isalpha():
                sb.append(ch)
                tl += 1
            else:
                if sb:
                    stk.append("".join(sb))
                    stk.append(tl)
                    tl += tl*(int(ch)-1)
                    stk.append(tl)
                    sb = []
                else:
                    tl += tl*(int(ch)-1)
                    stk.append(tl)
            if k == tl:
                if sb: return sb[-1]
                else: break
            if k < tl:
                # print(stk)
                stk.pop()
                break
        while stk:
            last = stk.pop()
            if type(last) == int:
                tl = last
                k %= tl
                # print(k,tl)
            else:
                if k == 0:
                    return last[-1]
                tail = len(last)
                if k > tl-tail:
                    n = k-(tl-tail)
                    return last[n-1]
        return last[k-1]
