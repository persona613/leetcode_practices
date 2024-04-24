"""
42 ms runtime beats 57.11%
16.88 MB memory beats 75.19%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(curr, parent):
            if parent:
                g[curr].append(parent)
                g[parent].append(curr)
            if curr.left:
                dfs(curr.left, curr)
            if curr.right:
                dfs(curr.right, curr)

        # build graph
        g = defaultdict(list)
        dfs(root, None)
        q = deque([target])
        seen = {target}
        d = 0
        while q and d < k:
            ln = len(q)
            for _ in range(ln):
                curr = q.popleft()
                for adj in g[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        q.append(adj)
            d += 1
        return [node.val for node in q]
        