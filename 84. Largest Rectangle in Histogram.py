"""
3061 ms runtime beats 5.03%
81.54 MB memory beats 6.28%
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def calculate(heights, node, qs, qe):
            if qs > qe:
                return 0

            mi = self.query(heights, n, node, qs, qe)
            return max(
                heights[mi] * (qe - qs + 1),
                calculate(heights, node, qs, mi - 1),
                calculate(heights, node, mi + 1, qe)
            )

        n = len(heights)
        root = self.buildST(heights, n, 0, n - 1)
        return calculate(heights, root, 0, n - 1)

    def buildST(self, arr, n, start, end):
        if start < 0 or end >= n or start > end:
            return
        if start == end:
            node = SegTreeNode(start, end)
            node.minidx = start
            return node
        
        node = SegTreeNode(start, end)
        mid = (start + end) // 2
        node.left = self.buildST(arr, n, start, mid)
        node.right = self.buildST(arr, n, mid + 1, end)

        if arr[node.left.minidx] < arr[node.right.minidx]:
            node.minidx = node.left.minidx
        else:
            node.minidx = node.right.minidx
        return node

    def query(self, arr, n, node, qs, qe):
        if not node or qe < node.start or qs > node.end:
            return -1
        if qs <= node.start and node.end <= qe:
            return node.minidx
        
        li = self.query(arr, n, node.left, qs, qe)
        ri = self.query(arr, n, node.right, qs, qe)
        if li == -1: return ri
        if ri == -1: return li
        if arr[li] < arr[ri]:
            return li
        return ri
                
class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.minidx = None
        self.left = None
        self.right = None