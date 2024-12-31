"""
243 ms runtime beats 14.92%
22.20 MB memory beats 11.52%
"""
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        g = defaultdict(list)
        parents = {region[0] for region in regions}
        for region in regions:
            curr = region[0]
            for reg in region[1:]:
                # root check
                if reg in parents:
                    parents.remove(reg)
                g[curr].append(reg)
        
        def dfs(g, root, r1, r2):
            if root == r1 or root == r2:
                return root

            found = set()
            for child in g[root]:
                ret = dfs(g, child, r1, r2)
                if ret:
                    if ret != r1 and ret != r2:
                        return ret
                    found.add(ret)

            if len(found) == 2:
                return root
            elif len(found) == 1:
                return found.pop()

        return dfs(g, parents.pop(), region1, region2)