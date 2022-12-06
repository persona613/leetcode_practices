'''
Runtime: 115 ms, faster than 37.11% of Python3 online submissions 
Memory Usage: 22.9 MB, less than 38.22% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hsm = defaultdict(list)
        
        def tri(root):
            if not root:
                return "#"            
            struct = ",".join([str(root.val), tri(root.left), tri(root.right)])
            hsm[struct].append(root)
            
            return struct
        
        tri(root)
        return [nodes[0] for nodes in hsm.values() if len(nodes)>1]
        