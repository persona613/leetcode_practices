class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = len(nums)
        i = 0
        result = False

        while i < t - 1 and result == False:
            cpnums = nums[i + 1:]
            n2 = target - nums[i]
            if n2 in cpnums:
                return [i, nums.index(n2, i + 1)]
                result = True
                break
            i = i + 1


nums = [2, 7, 11, 15]
target = 9

s1 = Solution()
s1.twoSum(nums, target)
