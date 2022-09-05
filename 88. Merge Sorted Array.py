'''
runtime beats 14.55%
memory usage beats 5.94%
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        nums1[:] = nums1[:m]
        for n2 in nums2:
            while i < len(nums1):
                if n2 <= nums1[i]:
                    nums1.insert(i, n2)
                    i += 1
                    break
                i += 1
            else:
                nums1.append(n2)