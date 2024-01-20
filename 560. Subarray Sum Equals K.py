"""
269 ms runtime beats 25.34%
20.72 MB memory beats 9.57%
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # curr: pre-sum on fly
        ans = curr = 0
        # dict of counts of [curr - k]
        d = defaultdict(int)
        d[0] = 1
        for v in nums:
            curr += v
            ans += d[curr - k]
            d[curr] += 1
        return ans