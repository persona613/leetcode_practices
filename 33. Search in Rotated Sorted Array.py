"""
88 ms runtime beats 37.3%
14.2 MB memory beats 56.23%
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min-index means k
        def mindex(nums):
            if len(nums) == 1:
                return 0
            st = 0
            nd = len(nums) - 1
            mid = (st+nd) // 2
            while st != mid:
                if nums[st] < nums[mid] and nums[mid] > nums[nd]:
                    st = mid + 1
                    mid = (st+nd) // 2
                elif nums[st] > nums[mid] and nums[mid] < nums[nd]:
                    nd = mid
                    mid = (st+nd) // 2
                elif nums[st] < nums[mid] and nums[mid] < nums[nd]:
                    return st
            if nums[st] >= nums[nd]:
                return nd
            else:
                return st
        
        n = len(nums)
        k = mindex(nums)
        st = 0
        nd = n - 1
        mid = (st+nd) // 2
        while st <= nd:
            if nums[(mid+k)%n] == target:
                return (mid+k)%n
            elif nums[(mid+k)%n] > target:
                nd = mid - 1
                mid = (st+nd) // 2
            else:
                st = mid + 1
                mid = (st+nd) // 2
        return -1
                