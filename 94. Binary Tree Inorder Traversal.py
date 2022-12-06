'''
Runtime: 35 ms, faster than 87.09% of Python3 online submissions 
Memory Usage: 14 MB, less than 0% of Python3 online submissions 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        leftseen = set()
        stk = [root]
        ans = []
        
        while stk:
            curr = stk[-1]
            leftseen.add(curr)
            if curr.left and curr.left not in leftseen:
                stk.append(curr.left)
                continue
            
            ans.append(curr.val)
            stk.pop()
            
            if curr.right:
                stk.append(curr.right)
                continue
        return ans