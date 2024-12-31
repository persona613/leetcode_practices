"""
231 ms runtime beats 73.38%
18.91 MB memory beats 9.74%
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # first, second: char
        def get_score(arr, first, second, score):
            # total_score
            ts = 0
            stk = []
            for c in arr:
                if stk and stk[-1] == first and c == second:
                    stk.pop()
                    ts += score
                else:
                    stk.append(c)
            return ts, stk

        if x >= y:
            ts, arr = get_score(list(s), "a", "b", x)
            return ts + get_score(arr, "b", "a", y)[0]
        else:
            ts, arr = get_score(list(s), "b", "a", y)
            return ts + get_score(arr, "a", "b", x)[0]