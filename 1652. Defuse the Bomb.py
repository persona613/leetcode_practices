"""
2 ms runtime beats 59.02%
16.71 MB memory beats 22.92%
"""
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0: return res
        if k > 0:
            ws = sum(code[:k])
            end = k - 1
        else:
            ws = sum(code[k - 1: -1])
            # pre first_array(res[0]) end 
            end = -2

        d = abs(k)
        for i in range(n):
            end = (end + 1) % n
            ws += code[end] - code[(end - d) % n]
            res[i] = ws
        return res
        