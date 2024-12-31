"""
60 ms runtime beats 64.84%
16.76 MB memory beats 11.25%
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, sm, comb):
            if sm == target:
                res.append(list(comb))
                return

            last_remove = 0
            for j in range(start, n):
                if last_remove == candidates[j]:
                    continue
                if sm + candidates[j] <= target:
                    comb.append(candidates[j])
                    backtrack(j + 1, sm + candidates[j], comb)
                    last_remove = comb.pop()

        candidates.sort()
        n = len(candidates)
        res = []
        backtrack(0, 0, [])
        return res