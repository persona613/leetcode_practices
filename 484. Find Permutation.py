"""
67 ms runtime beats 34.38%
17.99 MB memory beats 34.38%
"""
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [1]
        curr = 2
        # store number while meet "D"
        tmp = []
        for c in s:
            if c == "D":
                tmp.append(curr)
                curr += 1
            else:
                if tmp:
                    k = res.pop()
                    while tmp:
                        res.append(tmp.pop())
                    res.append(k)

                res.append(curr)
                curr += 1
        if tmp:
                k = res.pop()
                while tmp:
                    res.append(tmp.pop())
                res.append(k)
        return res