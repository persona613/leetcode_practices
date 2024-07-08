"""
3453 ms runtime beats 5.48%
35.60 MB memory beats 25.05%
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        def add(node, val):
            if not node:
                return TreeNode(val)

            if node.val == val:
                node.cnt += 1
                return node
            elif node.val < val:
                node.right = add(node.right, val)
            else:
                node.left = add(node.left, val)

            # update height
            node.height = max(get_height(node.left), get_height(node.right)) + 1

            # get balance
            b = get_balance(node)

            # AVL balance
            # left left
            if b > 1 and val < node.left.val:
                return rotate_right(node)
            # left right
            elif b > 1 and val > node.left.val:
                node.left = rotate_left(node.left)
                return rotate_right(node)
            # right right
            elif b < -1 and val > node.right.val:
                return rotate_left(node)
            # right left
            elif b < -1 and val < node.right.val:
                node.right = rotate_right(node.right)
                return rotate_left(node)
            return node
        
        def remove(node, val, cnt=1):
            if not node:
                return
            
            if node.val == val:
                if node.cnt > cnt:
                    node.cnt -= cnt
                    return node
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # have two children
                else:
                    sval, scnt = successor(node)
                    node.val = sval
                    node.cnt = scnt
                    node.right = remove(node.right, sval, scnt)

            elif node.val < val:
                node.right = remove(node.right, val)
            else:
                node.left = remove(node.left, val)
            
            # update height
            node.height = max(get_height(node.left), get_height(node.right)) + 1

            # get balance
            b = get_balance(node)

            # AVL balance
            # left left
            if b > 1 and get_balance(node.left) >= 0:
                return rotate_right(node)
            # left right
            elif b > 1 and get_balance(node.left) < 0:
                node.left = rotate_left(node.left)
                return rotate_right(node)
            # right right
            elif b < -1 and get_balance(node.right) <= 0:
                return rotate_left(node)
            # right left
            elif b < -1 and get_balance(node.right) > 0:
                node.right = rotate_right(node.right)
                return rotate_left(node)
            return node

        def successor(node) -> tuple[int]:
            node = node.right
            while node.left:
                node = node.left
            return node.val, node.cnt

        # t = inner children tree
        def rotate_left(z):
            y = z.right
            t = y.left

            # rotate
            y.left = z
            z.right = t

            # adjust height
            z.height = max(get_height(z.left), get_height(z.right)) + 1
            y.height = max(get_height(y.left), get_height(y.right)) + 1
            return y

        def rotate_right(z):
            y = z.left
            t = y.right

            # rotate
            y.right = z
            z.left = t

            # adjust height
            z.height = max(get_height(z.left), get_height(z.right)) + 1
            y.height = max(get_height(y.left), get_height(y.right)) + 1
            return y
        
        def get_height(node):
            if not node:
                return 0
            return node.height

        def get_balance(node):
            if not node:
                return 0
            return get_height(node.left) - get_height(node.right)

        def suc_val(root, origin: int) -> int:
            if not root:
                return
            
            if root.val <= origin:
                if root.val == origin and root.cnt > 1:
                    return root.val
                return suc_val(root.right, origin)
            else:
                parent = root.val
                ret = suc_val(root.left, origin)
                if ret == None:
                    return parent
                return ret

        def pre_val(root, origin: int) -> int:
            if not root:
                return
            
            if root.val >= origin:
                if root.val == origin and root.cnt > 1:
                    return root.val
                return pre_val(root.left, origin)
            else:
                parent = root.val
                ret = pre_val(root.right, origin)
                if ret == None:
                    return parent
                return ret

        def mindiff(root, val) -> int:
            mdiff = inf
            sval = suc_val(root, val)
            if sval != None:
                mdiff = min(mdiff, sval - val)
            if mdiff == 0:
                return mdiff

            pval = pre_val(root, val)
            if pval != None:
                mdiff = min(mdiff, val - pval)
            # print(f"val={val}, sval={sval}, pval={pval}")
            return mdiff

        n = len(nums)
        # window size
        size = indexDiff + 1
        root = TreeNode(nums[0])
        for i in range(1, n):
            # shrink window
            if i >= size:
                root = remove(root, nums[i - size])
            vi = nums[i]
            root = add(root, vi)
            # print(f"i={i}")
            d = mindiff(root, vi)
            # print(f"d={d}")
            if d <= valueDiff:
                return True
        return False

class TreeNode:
    def __init__(self, val=None, left=None, right=None, cnt=1, height=1):
        self.val = val
        self.left = left
        self.right = right
        # duplicate val
        self.cnt = cnt
        self.height = height