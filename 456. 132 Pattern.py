"""
422 ms runtime beats 26.79%
51.3 MB memory beats 10.8%
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        # index(exclusive) min dict
        mdic = dict()
        mdic[0] = float("inf")
        for i, n in enumerate(nums):
            mi = mdic[i]
            if n < mi:
                mdic[i+1] = n
            else:
                mdic[i+1] = mi
        stk = []
        for i in range(len(nums)-1, 0, -1):
            mi = mdic[i]
            rt = nums[i]
            while stk and mi >= stk[-1]:
                stk.pop()
            if not stk:
                stk.append(rt)
            elif rt > mi:
                if rt > stk[-1]:
                    return True
                else:
                    stk.append(rt)
        return False