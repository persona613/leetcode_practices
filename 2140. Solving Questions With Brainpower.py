"""
1337 ms runtime beats 20.04%
139.35 MB memory beats 10.13%
"""
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            solve = questions[i][0] + dp(i + questions[i][1] + 1)
            skip = dp(i + 1)
            return max(solve, skip)
        
        return dp(0)