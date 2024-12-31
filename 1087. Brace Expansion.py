"""
40 ms runtime beats 60.34%
17.05 MB memory beats 41.13%
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        # split s to lists
        arr = []
        # open brace: None or list
        ob = None
        for c in s:
            if c == "{":
                ob = []
            elif c == "}":
                arr.append(sorted(ob)[:])
                ob = None
            elif c == ",":
                continue
            else:
                if ob is not None:
                    ob.append(c)
                else:
                    arr.append([c])

        def backtrack(i, arr, path):
            if i == len(arr):
                res.append("".join(path))
                return
            for c in arr[i]:
                path.append(c)
                backtrack(i + 1, arr, path)
                path.pop()

        res = []
        path = []
        backtrack(0, arr, path)
        return res