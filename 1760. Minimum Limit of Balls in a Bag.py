"""
663 ms runtime beats 59.47%
29.19 MB memory beats 34.09%
"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def divide(size):
            # 1 divide-operation add 1 bag
            op = 0
            for v in nums:
                # op += (v + size - 1) // size - 1
                if v <= size:
                    break
                op += (v - 1) // size
            return op <= maxOperations

        nums.sort(reverse = True)
        # bag's max size
        l = 1
        r = max(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if divide(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l