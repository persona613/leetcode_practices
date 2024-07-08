"""
1056 ms runtime beats 5.87%
32.44 MB memory beats 87.72%
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        make1, make2 = nums[0], float("inf")
        for val in nums[1:]:
            if val > make2:
                return True
            elif val < make1:
                make1 = val
            elif val > make1:
                make2 = min(make2, val)
        return False