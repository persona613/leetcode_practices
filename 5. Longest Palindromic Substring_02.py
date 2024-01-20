"""
958 ms runtime beats 42.46%
76.6 MB memory beats 6.6%
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # print(n)
        memo = defaultdict(list)
        for i in range(n-1):
            if s[i] == s[i+1]:
                memo[2].append((i,i+1))
                st = i-1
                nd = i+2
                while st>=0 and nd<n:
                    if s[st]==s[nd]:
                        memo[nd-st+1].append((st,nd))
                        st -= 1
                        nd += 1
                    else:
                        break
            st = i-1
            nd = i+1
            while st>=0 and nd<n:
                if s[st]==s[nd]:
                    memo[nd-st+1].append((st,nd))
                    st -= 1
                    nd += 1
                else:
                    break
        if memo:
            k = max(memo.keys())
            st, nd = memo[k][0]
            return s[st:nd+1]
        return s[0]