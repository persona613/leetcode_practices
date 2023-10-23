"""
257 ms runtime beats 91.2%
20.3 MB memory beats 33.83%
"""
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = set(range(n))
        children = set(leftChild).union(set(rightChild))
        roots = nodes - children
        if len(roots) != 1:
            return False
        # BFS
        q = deque(list(roots))
        seen = set()
        while q:
            curr = q.popleft()
            lc, rc = leftChild[curr], rightChild[curr]
            if lc != -1:
                q.append(lc)
            if rc != -1:
                q.append(rc)
            if curr in seen:
                return False
            else:
                seen.add(curr)
        if len(seen) != n:
            return False                
        return True