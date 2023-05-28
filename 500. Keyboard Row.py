"""
43 ms runtime beats 25.71%
16.2 MB memory beats 22.6%
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            for k in range(3):
                if word[0].lower() in rows[k]:
                    break
            find = 1 # check gate
            for i in range(1, len(word)):
                if word[i].lower() not in rows[k]:
                    find = 0
                    break
            if find == 1:
                res.append(word)
        return res