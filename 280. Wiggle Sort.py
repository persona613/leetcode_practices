"""
71 ms runtime beats 86.69%
17.69 MB memory beats 66.04%
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mx = max(nums)
        bucks = [0] * (mx + 1)
        for v in nums:
            bucks[v] += 1
        n = len(nums)
        l = curr = 0
        r = mx
        while curr < n:
            while bucks[l] == 0:
                l += 1
            nums[curr] = l
            curr += 1
            bucks[l] -= 1

            if curr >= n:
                break

            while bucks[r] == 0:
                r -= 1
            nums[curr] = r
            curr += 1
            bucks[r] -= 1