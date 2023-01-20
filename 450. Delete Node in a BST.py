"""
80 ms runtime beats 69.43%
18.5 MB memory beats 22.86%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(node):
            # 1.find nextnode is node.right or node.right.left-most
            # 2.exchange node and nodenext's val
            # 3.check nextnode's children numbers
            # 4.delete nextnode from it's parent
            stk = [node]
            curr = node.right
            while curr:
                stk.append(curr)
                curr = curr.left
            nxt1 = stk.pop()
            node.val = nxt1.val
            if not nxt1.left and not nxt1.right:
                if nxt1 == node.right:
                    node.right = None
                else:
                    nxt2 = stk.pop()
                    nxt2.left = None
                    
            elif nxt1.right:
                if nxt1 == node.right:
                    node.right = node.right.right
                else:
                    nxt2 = stk.pop()
                    nxt2.left = nxt1.right
                    
        def search(root, key):
            if not root:
                return 
            if root.val == key:
                if not root.left and not root.right:
                    return 
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    delete(root)
                    return root
            if key < root.val:
                root.left = search(root.left, key)
            else:
                root.right = search(root.right, key)
            return root

        return search(root, key)
            
        