"""
39 ms runtime beats 68.62%
16.53 MB memory beats 32.99%
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        res = sorted(nums, key = NumStrCompare, reverse = True)

        ans = "".join([str(v) for v in res])
        if ans[0] == "0":
            return "0"
        return ans

class NumStrCompare(str):
    def __lt__(self, other):
        return self + other < other + self

# class NumStrCompare(int):
    # def __lt__(self, other):
        # return self * 10 ** len(str(other)) + other \
            # < other * 10 ** len(str(self)) + self