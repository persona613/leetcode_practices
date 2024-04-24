"""
291 ms runtime beats 62.68%
30.38 MB memory beats 55.57%
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # array store [1..n]
        for i in range(n):
            pointer = abs(nums[i]) - 1
            if pointer < n:
                if nums[pointer] > 0:
                    nums[pointer] *= -1
                    
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1