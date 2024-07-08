"""
674 ms runtime beats 87.75%
18.80 MB memory beats 57.33%
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(node, path, i, j):
            if trie.end in node:
                res.add("".join(path))
                del node[trie.end]

            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and not seen[ni][nj] \
                        and board[ni][nj] in node:
                    c = board[ni][nj]
                    path.append(board[ni][nj])
                    seen[ni][nj] = True
                    dfs(node[c], path, ni, nj)
                    path.pop()
                    seen[ni][nj] = False
                    if len(node[c]) == 0:
                        del node[c]

        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        seen = [[False] * n for _ in range(m)]
        res= set()
        path = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root:
                    c = board[i][j]
                    path.append(c)
                    seen[i][j] = True
                    dfs(trie.root[c], path, i, j)
                    path.pop()
                    seen[i][j] = False
                    if len(trie.root[c]) == 0:
                        del trie.root[c]
        return res


class Trie:

    def __init__(self):
        self.root = dict()
        self.end = "END"
    
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, dict())
        curr[self.end] = True