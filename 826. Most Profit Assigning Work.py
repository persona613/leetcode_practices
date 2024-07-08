"""
316 ms runtime beats 36.43%
19.63 MB memory beats 56.95%
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()

        # max profit before curr index(exclude)
        maxpft = [0]
        n = len(jobs)
        for i in range(n):
            # curr profit = jobs[i][1]
            maxpft.append(max(maxpft[-1], jobs[i][1]))

        ans = 0
        for wk in worker:
            idx = bisect.bisect_right(jobs, wk, key=lambda x: x[0])
            ans += maxpft[idx]
        return ans