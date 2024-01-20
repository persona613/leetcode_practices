"""
181 ms runtime beats 75.55%
21.94 MB memory beats 5.26%
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
        ans = 0
        for i in dic:
            if len(dic[i])==1:
                continue
            l = dic[i][0]
            r = dic[i][-1]
            if l+1==r:
                continue
            for j in dic:
                for p in dic[j]:
                    if l<p<r:
                        ans += 1
                        break
        return ans
            