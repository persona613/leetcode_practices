"""
106 ms runtime beats 50.62%
15.8 MB memory beats 19.40%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
       
        def grow(lo, hi):
            if lo >= hi:
                return
            midpool = []
            leftpool = []
            rightpool = []
            for i in range(lo, hi):
                # node = TreeNode(i)
                leftpool = grow(lo, i)
                rightpool = grow(i+1, hi)
                
                if leftpool and rightpool:
                    for lnode in leftpool:
                        for rnode in rightpool:
                            node = TreeNode(i)
                            node.left = lnode
                            node.right = rnode
                            midpool.append(node)
                            
                elif not leftpool and not rightpool:
                    node = TreeNode(i)
                    midpool.append(node)
                    
                elif not rightpool:
                    for lnode in leftpool:
                        node = TreeNode(i)
                        node.left = lnode
                        midpool.append(node)  
                        
                elif not leftpool:
                    for rnode in rightpool:
                        node = TreeNode(i)
                        node.right = rnode
                        midpool.append(node)
            return midpool
        
        return grow(1, n+1)