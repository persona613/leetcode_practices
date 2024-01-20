"""
Wrong Answer
138 / 142 testcases passed
Editorial
Input
s = "a"
Output
""
Expected
"a"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        N = 2*N + 1
        L = [0]*N
        L[0] = 0
        L[1] = 1
        mxLPSlen = 0
        mxLPScenter = 0
        C = 1
        R = 2
        for i in range(2, N):
            diff = R - i
            if diff > 0:
                mirrowI = 2*C - i
                L[i] = min(L[mirrowI], diff)

            di = L[i]
            while (i+di<N-1 and i-di>0) \
                and ((i+di+1)%2==0 \
                or s[(i+di+1)//2]==s[(i-di-1)//2]):
                di += 1
            L[i] = di

            if di > mxLPSlen:
                mxLPSlen = di
                mxLPScenter = i
            if i + di > R:
                R = i + di
                C = i
        st = (mxLPScenter - mxLPSlen) // 2
        # nd = (mxLPScneter + mxLPSlen) // 2 - 1
        nd = st + mxLPSlen - 1 
        return s[st:nd+1]