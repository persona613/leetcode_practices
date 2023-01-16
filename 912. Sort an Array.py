"""
1929 ms runtime beats 69.63%
22.7 MB memory beats 40.65%
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            li = ri = 0
            ret = []
            while li < len(left) and ri < len(right):
                if left[li] < right[ri]:
                    ret.append(left[li])
                    li += 1
                else:
                    ret.append(right[ri])
                    ri += 1
            ret.extend(left[li:])
            ret.extend(right[ri:])
            return ret
                
        if len(nums) < 2:
            return nums
        
        pivot = int(len(nums)/2)
        left = self.sortArray(nums[0:pivot])
        right = self.sortArray(nums[pivot:])
        return merge(left, right)
    
        