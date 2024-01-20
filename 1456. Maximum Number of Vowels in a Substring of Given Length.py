"""
102 ms runtime beats 95.13%
17.14 MB memory beats 49.38%
"""   
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = cnt = 0
        vos = "aeiou"
        for i in range(k):
            if s[i] in vos:
                cnt += 1
        ans = cnt
        for r in range(k, len(s)):
            if s[r] in vos:
                cnt += 1
            if s[l] in vos:
                cnt -= 1
            if cnt > ans:
                ans = cnt
                if ans == k:
                    return k
            l += 1
        return ans