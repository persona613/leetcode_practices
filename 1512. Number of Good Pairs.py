"""
38 ms runtime beats 75.74%
16.3 MB memory beats 53.10%
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for v in cnt.values():
            ans += v*(v-1)//2
        return ans