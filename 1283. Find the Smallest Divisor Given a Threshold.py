"""
263 ms runtime beats 60.81%
22.96 MB memory beats 34.28%
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def cal(div):
            sm = 0
            for v in nums:
                sm += math.ceil(v / div)
            return sm <= threshold

        l = 1
        r = 10 ** 6
        while l <= r:
            mid = (l + r) // 2
            if cal(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l