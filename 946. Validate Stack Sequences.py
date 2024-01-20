"""
58 ms runtime beats 98.17%
17.62 MB memory beats 13.75%
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = j = 0
        n = len(pushed)
        # i for compare popped string, j for pushed string
        while i < n and j < n:
            if stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1
            else:
                stk.append(pushed[j])
                j += 1
        while stk:
            if stk[-1] == popped[i]:
                stk.pop()
                i += 1
            else:
                return False
        return True
