"""
73 ms runtime beats 9.51%
16.76 MB memory beats 8.42%
"""
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        cnt = [0] * 26
        ans = 0
        base = ord("a")
        for i in range(k):
            cnt[ord(s[i]) - base] += 1
        if all(map(lambda x: x < 2, cnt)):
            ans += 1
        
        for i in range(k, len(s)):
            cnt[ord(s[i]) - base] += 1
            cnt[ord(s[i - k]) - base] -= 1
            if all(map(lambda x: x < 2, cnt)):
                ans += 1
        return ans