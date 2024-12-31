"""
260 ms runtime beats 66.67%
36.54 MB memory beats 60.36%
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = dict()
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, dict())
            curr["#"] = True

        def dfs(root, path):
            nonlocal maxword
            is_leaf = True
            for c in root:
                if c == "#":
                    continue
                if "#" in root[c]:
                    is_leaf = False
                    path.append(c)
                    dfs(root[c], path)
                    path.pop()
            if is_leaf:
                if len(path) > len(maxword):
                    maxword = "".join(path)
                elif len(path) == len(maxword):
                    maxword = min(maxword, "".join(path))

        maxword = ""
        dfs(trie, [])
        return maxword