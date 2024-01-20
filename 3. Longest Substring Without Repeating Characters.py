"""
236 ms runtime beats 14.30%
17.64 MB memory beats 7.98%
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # d={char:index of char}
        # -1 means no char appear before curr
        d = defaultdict(lambda: [-1, -1])
        ans = 0
        for i in range(len(s)):
            c = s[i]
            k = d[c][-1]
            # check other char position
            # position[-2] means repate
            for cha in d:
                if d[cha][-2] > k:
                    k = d[cha][-2]
            if i - k > ans:
                ans = i - k
            d[c].append(i)
        return ans