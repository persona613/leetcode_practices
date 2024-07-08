"""
24.9 ms runtime beats 26.58%
21.45 MB memory beats 50.59%
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def helper(root):
            tmp = []
            if "END" in root:
                tmp.append(root["END"])

            for char in root:
                if char == "END":
                    continue
                ret = helper(root[char])
                tmp.extend(ret)
                if len(tmp) >= 3:
                    break
            return tmp[:3]

        trie = dict()
        products.sort()
        for i, pd in enumerate(products):
            curr = trie
            for c in pd:
                curr = curr.setdefault(c, dict())
            curr["END"] = i

        n = len(searchWord)
        res = []
        root = trie
        for i in range(n):
            if searchWord[i] not in root:
                break
            root = root[searchWord[i]]
            ret = helper(root)
            res.append([products[j] for j in ret])

        if len(res) < n:
            res.extend([] for _ in range(n - len(res)))
        return res