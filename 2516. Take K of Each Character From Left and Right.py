"""
204 ms runtime beats 71.11%
17.23 MB memory beats 55.20%
"""
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        if any([v < k for v in cnt]):
            return -1

        # find longest subarray to remove
        ls = 0
        # chars' cnt >= k
        chars = 3
        l = 0
        for r in range(len(s)):
            c = s[r]
            if cnt[ord(c) - ord("a")] == k:
                chars -= 1
            cnt[ord(c) - ord("a")] -= 1
            
            while l <= r and chars < 3:
                c = s[l]
                if cnt[ord(c) - ord("a")] == k - 1:
                    chars += 1
                cnt[ord(c) - ord("a")] += 1
                l += 1
            
            ls = max(ls, r - l + 1)
        return len(s) - ls