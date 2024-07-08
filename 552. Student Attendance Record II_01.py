"""
Memory Limit Exceeded
45 / 59 testcases passed
Last Executed Input
Use Testcase
n =
99991
"""
class Solution:
    def checkRecord(self, n: int) -> int:

        # idx, A=0,L=1,P=2, have_Absent:True=1,False=0
        @lru_cache(None)
        def dp(i, code, ha):
            if i < 0:
                if code == 2: return 1
                return 0
            if i == 0:
                if code == 0:
                    return 1 if ha == 1 else 0
                return 1
            # A  
            if code == 0:
                return (dp(i-1, 1, 1) + dp(i-1, 2, 1)) % mod
            # L
            elif code == 1:
                # one-L + two-L
                # P + curr-L, PL + curr-L
                if ha:
                    return (dp(i-1, 2, 1) + dp(i-2, 2, 1)) % mod
                # one-L + two-L
                # P,A + curr-L, PL,AL + curr-L
                else:
                    return (dp(i-1, 0, 1) + dp(i-1, 2, 0) \
                            + dp(i-2, 0, 1) + dp(i-2, 2, 0)) % mod
            # P
            else:
                if ha:
                    return (dp(i-1, 1, 1) + dp(i-1, 2, 1)) % mod
                else:
                    return (dp(i-1, 1, 0) + dp(i-1, 2, 0) \
                            + dp(i-1, 0, 1)) % mod

        mod = 10 ** 9 + 7
        ans = 0
        for code in range(3):
            if code == 0:
                ans += dp(n-1, code, 1) % mod
            else:
                ans += dp(n-1, code, 0) % mod
        return ans % mod
