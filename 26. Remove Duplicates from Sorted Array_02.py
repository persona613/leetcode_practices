'''
Runtime: 93 ms, faster than 92.15% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 0% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        detect = head + 1
        d = False
        le = len(nums)
        while detect < le:
            if nums[head] == nums[detect]:
                d = True
                detect += 1
            else:
                if d:
                    del nums[head:detect-1]
                    le -= detect-1-head
                    d = False
                head += 1
                detect = head + 1
        if d:
            del nums[head:detect-1]
            le -= detect-1-head
            d = False
            return le
        return le
        
            