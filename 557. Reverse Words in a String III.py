'''
Runtime: 49 ms, faster than 41.32% of Python3 online submissions
Memory Usage: 17 MB, less than 67.63% of Python3 online submissions
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        tmp = []
        for c in s:
            if c == " ":
                res.append("".join(tmp[::-1]))
                tmp = []
            else:
                tmp.append(c)
        res.append("".join(tmp[::-1]))
        return " ".join(res)