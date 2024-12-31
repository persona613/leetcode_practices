"""
356 ms runtime beats 25.07%
22.86 MB memory beats 6.96%
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        # prefix sum
        ps = [0] * (n + 1)
        vowels = dict()
        for i, c in enumerate("aeiou"):
            vowels[c] = 1 << i
        
        for i in range(n):
            c = s[i]
            if c in vowels:
                ps[i + 1] = ps[i] ^ vowels[c]
            else:
                ps[i + 1] = ps[i]

        # pre val index record val's pos
        pval_idx = dict()
        mxln = 0
        for i in range(n + 1):
            val = ps[i]
            # record left most idx
            if val not in pval_idx:
                pval_idx[val] = i
            else:
                mxln = max(mxln, i - pval_idx[val])
        return mxln