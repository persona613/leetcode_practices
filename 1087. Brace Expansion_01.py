"""
Wrong Answer
55 / 56 testcases passed

Editorial
Input
s =
"{a,b}{z,x,y}"

Use Testcase
Output
["az","ax","ay","bz","bx","by"]
Expected
["ax","ay","az","bx","by","bz"]
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        # split s to lists
        arr, bag = [], []
        # open brace
        ob = False
        for c in s:
            if c == "{":
                ob = True
            elif c == "}":
                ob = False
                arr.append(bag[:])
                bag = []
            elif c == ",":
                continue
            else:
                if ob:
                    bag.append(c)
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