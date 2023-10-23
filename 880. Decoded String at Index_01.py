"""
Runtime Error
7 / 45 testcases passed
IndexError: list index out of range
    if k == tl: return sb[-1]
Last Executed Input
Use Testcase
s = "a23"
k = 6
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
            if k == tl: return sb[-1]
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
                tail = len(last)
                if k > tl-tail:
                    n = k-(tl-tail)
                    return last[n-1]
        return last[k-1]
