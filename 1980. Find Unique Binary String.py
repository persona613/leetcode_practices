"""
31 ms runtime beats 97.71%
16.30 MB memory beats 42.98%
"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            cur = nums[i][i]
            res.append("0" if cur=="1" else "1")
        return "".join(res)