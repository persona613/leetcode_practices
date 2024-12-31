"""
31 ms runtime beats 90.48%
17.28 MB memory beats 8.08%
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        @lru_cache(None)
        def dfs(exp):
            ways = dict()
            for i in range(len(exp)):
                # cut at every operation index
                if exp[i] in op_map:
                    oper = op_map[exp[i]]
                    left = dfs(exp[:i])
                    right = dfs(exp[i + 1:])
                    # corss product
                    for l in left:
                        for r in right:
                            # formula
                            f = "(" + l + exp[i] + r + ")"
                            if f not in ways:
                                ways[f] = oper(left[l], right[r])
            if not ways:
                return {exp: int(exp)}
            return ways

        op_map = {"+": add, "-": sub, "*": mul}
        ret = dfs(expression)
        return ret.values()
        