"""Wrong Answer
Last Executed Input
[5,6,0,2]
0
Output:
-1
Expected:
2
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min-index means k
        def mindex(nums):
            if len(nums) == 1:
                return 0
            if len(nums) == 2:
                if nums[0] < nums[1]:
                    return 0
                else:
                    return 1
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
            return nd
        
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
                