"""
62 ms runtime beats 46.62%
19.02 MB memory beats 16.70%
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
                curr.append(ch.val)
                if ch.children:
                    curr.append([])
                    preorder(curr[-1], ch)

        if not root:
            return
        # json.dumps(dict) => string, json.loads(string) => dict
        # dict for data
        lst = list()
        lst.append(root.val)
        if root.children:
            lst.append([])
            preorder(lst[-1], root)
        return json.dumps(lst)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        def create(node, curr):
            for elm in curr:
                if type(elm) == int:
                    new_node = Node(elm, [])
                    node.children.append(new_node)
                else:
                    create(new_node, elm)

        if not data:
            return
        lst = json.loads(data)
        dummy = Node(0, [])
        create(dummy, lst)
        return dummy.children[0]       



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))