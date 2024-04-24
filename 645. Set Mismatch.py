"""
154 ms runtime beats 89.22%
18.69 MB memory beats 51.72%
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        for v in nums:
            if v in seen:
                break
            seen.add(v)
        n = len(nums)
        t = n * (n + 1) //2
        k = t - (sum(nums) - v)
        return [v, k]
