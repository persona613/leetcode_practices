"""
53 ms runtime beats 96.43%
16.71 MB memory beats 53.41%
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        dic = defaultdict(int)
        n = len(s)
        j = ans = 0
        for i in range(n) :
            dic[s[i]] += 1
            if len(dic) > k:
                if dic[s[j]] > 1:
                    dic[s[j]] -= 1
                else:
                    del dic[s[j]]
                j += 1
        return n - j