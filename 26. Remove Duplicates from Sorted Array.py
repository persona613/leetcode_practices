# Runtime: 185 ms, faster than 18.95% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.5 MB, less than 61.73% of Python3 online submissions for Remove Duplicates from Sorted Array.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        lenth = len(nums)
        
        i = 0
        k = 0
        while i < lenth:
            j = i+1
            while j < lenth:
                if nums[i] == nums[j]:
                    j += 1
                else:
                    k += 1
                    nums[k] = nums[j]
                    i = j-1
                    
                    break
            i += 1
        
        return k+1
        return list(nums)
            
        

        
#  while i < lenth:
#             j = i+1
#             while j < lenth:
#                 if nums[i] == nums[j]:
#                     j += 1
#                 else:
#                     k += 1
#                     ch = nums[k]
#                     nums[k] = nums[j]
#                     nums[j] = ch
#                     i = j+1
                    
#                     break
#             i += 1
                