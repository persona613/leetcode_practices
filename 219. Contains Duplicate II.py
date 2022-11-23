'''
Runtime: 723 ms, faster than 83.12% of Python3 online submissions 
Memory Usage: 32.2 MB, less than 10.66% of Python3 online submissions
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        for i, n in enumerate(nums):
            if n in count:
                count[n].append(i)
            else:
                count[n] = [i]
        for lst in list(count.values()):
            if len(lst) > 1:
                i = 1
                while i < len(lst):
                    if (lst[i] - lst[i-1]) <= k:
                        return True
                    i += 1
        return False