"""
51 ms runtime beats 94.25%
16.36 MB memory beats 75.95%
"""
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                i += 1
            else:
                if k % 2:
                    # check min of abs values
                    if nums[i] < nums[i-1]:
                        nums[i] = -nums[i]
                    else:
                        nums[i-1] = -nums[i-1]
                break
        else:
            if k % 2:
                nums[-1] = -nums[-1]
        return sum(nums)
