"""
Runtime Error
3 / 38 testcases passed
submitted at May 02, 2024 22:50

Last Executed Input
Use Testcase
[3,null,1,null,5]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        # postorder
        def find_n(node, n):
            if not node.children:
                return 0
            for ch_node in node.children:
                ret = find_n(ch_node, n)
                if ret > n:
                    n = ret
            return max(n, len(node.children))

        if not root:
            return
        n = find_n(root, 0)
        if n <= 2:
            return root
        
        curr = new_root = TreeNode([root.val, n])
        parent = deque()
        q = deque([(root, 0)])
        while q:
            node, idx = q.popleft()
            for i, ch_node in enumerate(node.children):
                ni = idx * n + (i + 1)
                q.append((ch_node, ni))

                new_node = TreeNode([ch_node.val, ni])
                if curr.left and curr.right:
                    curr = parent.popleft()
                if not curr.left:
                    curr.left = new_node
                    parent.append(curr.left)
                else:
                    curr.right = new_node
                    parent.append(curr.right)
        return new_root

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return

        n = data.val[1]
        data.val[1] = 0
        dic = {-1: Node(-1, [])}
        q = deque([data])
        while q:
            curr = q.popleft()
            val, idx = curr.val
            new_node = Node(val, [])
            dic[(idx - 1) // n].children.append(new_node)
            dic[idx] = new_node

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return dic[-1].children[0]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))