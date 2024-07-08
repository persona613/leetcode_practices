"""
83 ms runtime beats 59.13%
21.90 MB memory beats 9.94%
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = self.collect(root, 0, [])
        return " ".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        data = data.split(" ")
        dummy = TreeNode(0)
        dic = {-1: dummy}
        for i in range(0, len(data), 2):
            index =  int(data[i], 2)
            val = int(data[i + 1], 2)
            node = TreeNode(val)

            # parent_index
            if index % 2:
                pari = (index - 1) // 2
                dic[pari].left = node
            else:
                pari = (index - 2) // 2
                dic[pari].right = node
            dic[index] = node
        return dummy.right

    def collect(self, node, index, bag):
        if not node:
            return bag
        bag.append(bin(index))
        bag.append(bin(node.val))
        self.collect(node.left, index * 2 + 1, bag)
        self.collect(node.right, index * 2 + 2, bag)
        return bag


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))