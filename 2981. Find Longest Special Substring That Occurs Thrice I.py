"""
31 ms runtime beats 23.78%
17.08 MB memory beats 19.87%
"""
class Solution:
    def maximumLength(self, s: str) -> int:

        def sliding(size):
            freq = [0] * 26
            window = dict()
            for i in range(size):
                window[s[i]] = window.get(s[i], 0) + 1
            if len(window) == 1:
                key = next(iter(window))
                freq[ord(key) - ord("a")] += 1

            for r in range(size, n):
                window[s[r]] = window.get(s[r], 0) + 1
                window[s[r - size]] -= 1
                if window[s[r - size]] == 0:
                    del window[s[r - size]]
                if len(window) == 1:
                    key = next(iter(window))
                    freq[ord(key) - ord("a")] += 1
            return any(fr >= 3 for fr in freq)

        n = len(s)
        # binary search: upper mid
        l = 0
        r = n - 2
        while l < r:
            mid = (l + r + 1) // 2
            if sliding(mid):
                l = mid
            else:
                r = mid - 1
        return l if l else -1