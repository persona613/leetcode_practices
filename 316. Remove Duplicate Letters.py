"""
42 ms runtime beats 60.99%
16.2 MB memory beats 82.57%
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rd = {}
        for i, c in enumerate(s):
            if c not in rd:
                rd[c] = i
            else:
                rd[c] = i
        idx = {k:-1 for k in rd.keys()}
        stk = []
        for i, curr in enumerate(s):
            if curr in stk:
                idx[curr] = i
                continue
            while stk:
                last = stk[-1]
                if curr < last:
                    if idx[last] < rd[last]:
                        stk.pop()
                    else:
                        break
                else:
                    break
            stk.append(curr)
            idx[curr] = i
        return "".join(stk)
