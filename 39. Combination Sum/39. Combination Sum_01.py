"""
Wrong Answer

Input
candidates =
[8,7,4,3]
target =
11
45 / 160 testcases passed
Output
[[3,8]]
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def pick(t):
            for num in candidates: 
                if t - num < 0:            
                    return
                elif t - num == 0: 
                    combine.append(num)
                    if set(combine) not in seen:                   
                        res.append(combine[:])
                        seen.append(set(combine))
                    combine.pop()
                    return
                else:
                    combine.append(num)
                    pick(t - num)
                    combine.pop()
        
        res = []
        combine = []
        seen = []
        pick(target)
        return res