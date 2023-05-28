"""
96 ms runtime beats 40.49%
20.1 MB memory beats 5.10%
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = nums[:]
        for i in range(1, len(nums)):
            self.presum[i] += self.presum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presum[right]
        return self.presum[right] - self.presum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)