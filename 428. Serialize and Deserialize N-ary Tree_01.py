"""
Wrong Answer
26 / 38 testcases passed
submitted at May 02, 2024 18:06
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        def preorder(curr, node):
            for ch in node.children:
                next_curr = curr.setdefault(ch.val, dict())
                preorder(next_curr, ch)

        if not root:
            return
        # json.dumps(dict) => string, json.loads(string) => dict
        # dict for data
        dic = dict()
        curr = dic.setdefault(root.val, dict())
        preorder(curr, root)
        return json.dumps(dic)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        def create(node, curr):
            for key in curr:
                new_node = Node(key, [])
                node.children.append(new_node)
                create(new_node, curr[key])

        if not data:
            return
        dic = json.loads(data)
        dummy = Node(0, [])
        create(dummy, dic)
        return dummy.children[0]       



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))