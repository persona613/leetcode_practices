"""
Wrong Answer
800 / 811 testcases passed

Editorial
Input
s =
"eccdnmcnkl"

Use Testcase
Output
-1
Expected
1
"""
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # record cnt of special string
        freq = [[0] * 26 for _ in range(n + 1)]
        # sliding window
        l = 0
        char = s[0]
        for r in range(1, n):
            if s[r] != char:
                # same chars count: r - l
                freq[r - l][ord(char) - ord("a")] += 1

                char = s[r]
                l = r
        freq[n - l][ord(char) - ord("a")] += 1

        ans = 0
        for i in range(n, 0, -1):
            for j in range(26):
                cnt = freq[i][j]
                ln = 0
                if cnt >= 3:
                    ln = i
                elif cnt == 2:
                    ln = i - 1
                elif cnt == 1:
                    ln = i - 2
                ans = max(ans, ln)
        return ans if ans else -1