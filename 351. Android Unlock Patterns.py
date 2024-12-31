"""
342 ms runtime beats 58.72%
16.73 MB memory beats 21.13%
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # detect midkey
        def midkey(curr, nxt):
            ci = (curr - 1) // 3
            cj = (curr - 1) % 3
            ni = (nxt - 1) // 3
            nj = (nxt - 1) % 3
            fi = abs(ci - ni)
            fj = abs(cj - nj)
            if (fi == 0 and fj == 2) \
                    or (fi == 2 and fj == 0) \
                    or (fi == 2 and fj == 2):
                mi = (ci + ni) // 2
                mj = (cj + nj) // 2
                return 3 * mi + mj + 1
            return 0

        # bitmask, last digit, length of path
        def dfs(bt, d, ln):
            if ln > n:
                return

            cnt = 0
            for nxt in range(1, 10):
                mask = 1 << nxt
                if bt & mask:
                    continue
                if mid[d][nxt] and not bt & (1 << mid[d][nxt]):
                    continue
                cnt += 1
                dfs(bt | mask, nxt, ln + 1)
            dp[ln] += cnt

        # cnt of k keys
        dp = [0] * (n + 1)
        # mid key record
        mid = [[0] * 10 for _ in range(10)]
        for i in range(1, 10):
            for j in range(1, 10):
                mid[i][j] = midkey(i, j)

        dfs(0, 0, 1)
        return sum(dp[m: n + 1])