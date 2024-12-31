"""
36 ms runtime beats 57.84%
16.70 MB memory beats 32.16%
"""
class Solution:
    def pathSum(self, nums: List[int]) -> int:

        # return leaves count
        def dfs(tree, node):
            if node not in tree:
                return 0
            
            rch = node + 10 + node % 10
            rcnt = dfs(tree, rch)
            lcnt = dfs(tree, rch - 1)

            if rcnt + lcnt == 0:
                ans[0] += tree[node]
                return 1

            ans[0] += tree[node] * (rcnt + lcnt)
            return rcnt + lcnt

        # graph = {node(row, col): value}
        # R child = Parent + 10 + Parent % 10
        g = defaultdict(int)
        root = nums[0] // 10
        ans = [0]
        for v in nums:
            g[v // 10] = v % 10
        dfs(g, root)
        return ans[0]
            