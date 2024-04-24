"""
165 ms runtime beats 31.97%
23.17 MB memory beats 15.88%
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # check if char position not duplicate
        def check(curr, pre):
            if pre == 0:
                return False
            for i in range(26):
                bm = 1 << i
                if (curr & bm) > 0 and (pre & bm) > 0:
                    return False
            return True

        n = len(arr)
        dp = [0] * n
        memo = dict()
        # transfer string to bit-int
        for i in range(n):
            x = 0
            for ch in arr[i]:
                bm = 1 << (ord(ch) - 97)
                # detect if char position duplicate
                if (x & bm) > 0:
                    x = 0
                    break
                x ^= bm
            memo[1 << (n - 1 - i)] = x # key trans from arr-index-list
        
        # init, inverse dp
        dp[-1] = int.bit_count(memo[1 << 0])
        for i in range(n - 2, -1, -1):
            key = 1 << (n - 1 - i)
            if memo[key] == 0:
                dp[i] = dp[i + 1]
                continue
            curr = memo[key]
            cnt = int.bit_count(curr)
            for j in range(1, key):
                if j in memo and check(curr, memo[j]):
                    memo[key ^ j] = curr ^ memo[j]
                    cnt = max(cnt, int.bit_count(memo[key ^ j]))
            dp[i] = max(dp[i + 1], cnt)
        # print(memo, dp)
        return dp[0]
