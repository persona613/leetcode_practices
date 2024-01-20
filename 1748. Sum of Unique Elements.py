"""
36 ms runtime beats 88.16%
16.33 MB memory beats 15.69%
"""
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0
        for k in d:
            if d[k] == 1:
                ans += k
        return ans