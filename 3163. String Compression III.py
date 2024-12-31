"""
221 ms runtime beats 65.96%
27.30 MB memory beats 16.78%
"""
class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        cnt = 1
        for i in range(1, len(word)):
            if word[i] != word[i - 1] or cnt >= 9:
                res.append(str(cnt) + word[i - 1])
                cnt = 0
            cnt += 1
        res.append(str(cnt) + word[-1])
        return "".join(res)