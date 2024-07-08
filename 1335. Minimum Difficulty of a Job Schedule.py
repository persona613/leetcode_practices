"""
519 ms runtime beats 62.53%
18.02 MB memory beats 21.79%
"""
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        # pre compute remain job difficulty at last day
        jobdiff = [None] * n
        hardest = 0
        for i in range(n-1, -1, -1):
            hardest = max(hardest, jobDifficulty[i])
            jobdiff[i] = hardest

        @lru_cache(None)        
        def dp(i, day):
            if day == d:
                return jobdiff[i]

            best = float("inf")
            hardest_job = 0
            # pre reserve jobs for later days
            reserve = n - (d - day)
            for j in range(i, reserve):
                hardest_job = max(hardest_job, jobDifficulty[j])
                best = min(best, hardest_job + dp(j+1, day+1))
            return best

        return dp(0, 1)