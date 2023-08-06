"""
47 ms runtime beats 79.34%
16.3 MB memory beats 93.14%
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                continue
            n = min(len(words[i]), len(words[i+1]))
            for j in range(n):
                if m[words[i][j]] < m[words[i+1][j]]:
                    break
                elif m[words[i][j]] > m[words[i+1][j]]:
                    return False
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        return True
