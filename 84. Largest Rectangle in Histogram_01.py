"""
should correct brute-force, but un-submit
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def area(lst):
            if not lst:
                return 0
            return min(lst)*len(lst)
        
        def backtrack(hs):
            nonlocal ans
            if not hs:
                return 
            mini = min(hs)
            for i, h in enumerate(hs):
                for d in range(len(hs)-i):
                    area_ = area(hs[i:i+d+1])
                    print("lst:",hs[i:i+d+1],"area:",area_)
                    if ans < area_:
                        ans = area_
        
        ans = 0
        backtrack(heights)
        return ans