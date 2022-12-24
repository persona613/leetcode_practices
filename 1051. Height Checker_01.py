'''
Runtime: 59 ms, faster than 46.88% of Python3 online submissions 
Memory Usage: 13.8 MB, less than 96.52% of Python3 online submissions 
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortlist = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sortlist[i] != heights[i]:
                count += 1
        return count