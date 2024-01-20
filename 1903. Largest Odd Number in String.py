"""
53 ms runtime beats 64.91%
17.92 MB memory beats 19.52%
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""