"""
169 ms runtime beats 68.67%
17.79 MB memory beats 54.43%
"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stk = []
        pre_mid = None
        for a in preorder:
            # right branch: next big, record pre_mid
            while stk and stk[-1] < a:
                pre_mid = stk.pop()

            # left branch: next small should > pre_mid
            if pre_mid and pre_mid > a:
                return False
            stk.append(a)
        return True