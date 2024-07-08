"""
604 ms runtime beats 59.94%
18.90 MB memory beats 5.46%
"""
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = dict()
        n = len(jobDifficulty)
        lmax = []
        mx = -1
        for j in jobDifficulty:
            if j > mx:
                mx = j
            lmax.append(mx)
        # print("lmax:", lmax)
        rmax = [None] * n
        mx = -1
        for j in range(n-1, -1, -1):
            if jobDifficulty[j] > mx:
                mx = jobDifficulty[j]
            rmax[j] = mx
        # print("rmax:", rmax)

        def cut(i, ct):
            if (i, ct) in memo:
                return memo[(i, ct)]
            if ct == 0 and i < n:
                memo[(i, ct)] = -1
                return -1
            if i == n and ct > 0:
                memo[(i, ct)] = -1
                return -1
            if ct == 1 and i < n:
                # memo[(i, ct)] = max(jobDifficulty[i:n])
                memo[(i, ct)] = rmax[i]
                return memo[(i, ct)]

            # i not include curr index
            # next day difficulty
            df = inf
            curr_df = 0
            for j in range(i + 1, n + 1):
                if i == 0:
                    curr_df = lmax[j - 1]
                else:
                    # curr_df = max(jobDifficulty[i:j])
                    if jobDifficulty[j - 1] > curr_df:
                        curr_df = jobDifficulty[j - 1]
                ndf = cut(j, ct - 1)
                # print(j, ct - 1)
                if ndf >= 0:
                    df = min(df, curr_df + ndf)
            if df == inf: # all possible cut-way are -1
                memo[(i, ct)] = -1
                return -1
            memo[(i, ct)] = df
            return memo[(i, ct)]

        return cut(0, d)
