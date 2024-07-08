"""
46 ms runtime beats 34.92%
16.55 MB memory beats 40.10%
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find min_indx in elements(those > level)
        def min_index(start, level=-1):
            mi = 101
            midx = None
            for i in range(start, n):
                if nums[i] > level and nums[i] < mi:
                    mi = nums[i]
                    midx = i
            return midx

        n = len(nums)
        # sort nums[p:]
        p = 0

        # check any suffix val > curr in reverse order
        for i in range(n - 2, -1, -1):
            # curr = nums[i]
            # if True, replace curr with j:= minin of vals
            j = min_index(i + 1, nums[i])
            if j:
                nums[i], nums[j] = nums[j], nums[i]
                # sort vals after i
                p = i + 1
                break

        # not found j, return smallest permutation
        # found j, sort nums[p:]
        for i in range(p, n - 1):
            j = min_index(i)
            nums[i], nums[j] = nums[j], nums[i]