"""
1017 ms runtime beats 5%
17.28 MB memory beats 76.65%
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # "A"=65, "a"=97
        arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        g = dict()
        for c in arr:
            g[c] = ord(c) - ord("A")

        k = ord("z") - ord("A") # k=57
        cnt = [0] * (k + 1)
        for c in t:
            cnt[g[c]] += 1

        l = 0
        d = len(s) + 1
        res = [0, 0]
        for i in range(len(s)):
            cnt[g[s[i]]] -= 1
            if all([x <= 0 for x in cnt]):
                if i - l + 1 < d:
                    d = i - l + 1
                    res = [l, i + 1]

            while all([x <= 0 for x in cnt]):
                cnt[g[s[l]]] += 1
                l += 1
                if all([x <= 0 for x in cnt]):
                    if i - l + 1 < d:
                        d = i - l + 1
                        res = [l, i + 1]
        return s[res[0]:res[1]]