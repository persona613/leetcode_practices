"""
41 ms runtime beats 94.09%
16.65 MB memory beats 30.23%
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        candidates.sort()
        n = len(candidates)
        res = []
        backtrack(0, target, [])
        return res