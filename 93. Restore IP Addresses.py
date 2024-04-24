"""
28 ms runtime beats 97.20%
16.49 MB memory beats 93.01%
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtrack(i, dot, curr, path):
            if i == n:
                if dot == 0 and len(path) == 3 and curr:
                    path.append("".join(curr))
                    res.append("".join(path))
                    # print(f"finish i={i}, d={dot}, curr={curr}, path={path}")
                    path.pop()
                return

            curr.append(s[i])
            if len(curr) > 3: return
            if len(curr) > 1 and curr[0] == "0": return
            val = int("".join(curr))
            if val > 255: return

            if dot > 0:
                dot -= 1
                curr.append(".")
                path.append("".join(curr))
                # print(f"i={i}, d={dot}, curr={curr}, path={path}")
                backtrack(i + 1, dot, [], path)
                path.pop()
                curr.pop()
                dot += 1
                # print(f"After Dot i={i}, d={dot}, curr={curr}, path={path}")

            # print(f"Nodot: i={i}, d={dot}, curr={curr}, path={path}")
            backtrack(i + 1, dot, curr, path)

        n = len(s)
        if n > 12: return []
        res = []
        backtrack(0, 3, [], [])
        return res