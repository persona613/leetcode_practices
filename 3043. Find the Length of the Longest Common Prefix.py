"""
782 ms runtime beats 81.43%
28.47 MB memory beats 76.92%
"""
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()
        for a in arr1:
            while a > 0:
                prefix.add(a)
                a //= 10
        mxlen = 0
        for a in arr2:
            while a > 0:
                if a in prefix:
                    mxlen = max(mxlen, len(str(a)))
                a //= 10
        return mxlen