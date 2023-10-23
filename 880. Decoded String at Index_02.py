"""
Wrong Answer
38 / 45 testcases passed
Last Executed Input
Use Testcase
"a2b3c4d5e6f7g8h9"
k = 9
Output
"a"
Expected
"b"
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
                tail = len(last)
                if k > tl-tail:
                    n = k-(tl-tail)
                    return last[n-1]
        return last[k-1]

