"""
70 ms runtime beats 92.90%
20 MB memory beats 88.1%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = -1
        self.lst = []
        self.dfs(root)
    
    def dfs(self, root) -> None:
        if not root:
            return
        self.dfs(root.left)
        self.lst.append(root.val)
        self.dfs(root.right)

    def next(self) -> int:
        self.p += 1
        return self.lst[self.p]
        

    def hasNext(self) -> bool:
        return self.p < len(self.lst)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()