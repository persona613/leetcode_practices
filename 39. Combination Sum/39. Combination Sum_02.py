"""
Wrong Answer

Input
candidates =
[7,3,2]
target =
18
120 / 160 testcases passed
Output
[[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,7,7],[3,3,3,3,3,3]]
Expected
[[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def pick(t):
            if t < 0:
                return
            for num in nums: 
                combine.append(num)
                if t - num == 0:
                    if set(combine) not in seen:
                        res.append(combine[:])
                        seen.append(set(combine))
                    combine.pop()
                    return
                else:
                    pick(t - num)
                    combine.pop()
        
        res = []
        combine = []
        seen = []
        nums = sorted(candidates)
        pick(target)
        return res