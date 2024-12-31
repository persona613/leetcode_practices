"""
99 ms runtime beats 74.48%
41.70 MB memory beats 20.69%
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        def dfs(node, res):
            if END in node:
                res.append(node[END])
                return res

            for child_key in node:
                dfs(node[child_key], res)
            return res

        trie = dict()
        END = "end"
        for fo in folder:
            path = fo.split("/")
            curr = trie
            for p in path:
                curr = curr.setdefault(p, dict())
            curr[END] = fo
        return dfs(trie, [])