"""
Runtime Error
36 / 52 testcases passed
submitted at May 04, 2024 13:49

Editorial
AttributeError: 'NoneType' object has no attribute 'right'
    ^^^^^^^^^^^
    pivot.right = node
Line 86 in rotate (Solution.py)
           ^^^^^^^^^^^^^^^
    node = rotate(node, 1)
Line 30 in add (Solution.py)
                           ^^^^^^^^^^^^^^^^^^^
    node.left, duplicate = add(node.left, val)
Line 15 in add (Solution.py)
                           ^^^^^^^^^^^^^^^^^^^
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # output: node, duplicate(bool)
        def add(node, val):
            if not node:
                return TreeNode(val), None

            # duplicate = None
            if node.val == val:
                node.cnt += 1
                duplicate = True
            elif node.val < val:
                node.right, duplicate = add(node.right, val)
            else:
                node.left, duplicate = add(node.left, val)

            # size ignore duplicat vals
            if not duplicate:
                node.size += 1

            # balance, rotate left=0, right=1
            rsize = node.right.size if node.right else 0
            lsize = node.left.size if node.left else 0
            if rsize > lsize + 1:
                # print(f"lsize={lsize},rsize={rsize}")
                # print(f"rotate:{node.val}, 0")
                # print(dfs(node))
                node = rotate(node, 0)
            elif lsize > rsize + 1:
                node = rotate(node, 1)
                # print(f"rotate:{node.val}, 1")
                # print(dfs(node))
            return node, duplicate
        
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        
        def rotate(node, dir):
            # rotate left
            if dir == 0:
                # type I
                if node.right.right:
                    pivot = node.right
                    # inner child: pivot.left
                    node.right = pivot.left
                    pivot.left = node
                    # adjust size of node, pivot
                    total_size = node.size
                    node.size -= pivot.right.size + 1
                    pivot.size = total_size
                
                # type Z
                else:
                    pivot = node.right.left
                    side = node.right
                    node.right = None
                    side.left = None
                    pivot.left = node
                    pivot.right = side
                    # adjist size of node, pivot, side
                    total_size = node.size
                    node.size -= side.size
                    side.size -= pivot.size
                    pivot.size = total_size

            # rotate right
            else:
                # type I                
                if node.left.left:
                    pivot = node.left
                    # inner child: pivot.right
                    node.left = pivot.right
                    pivot.right = node
                    # adjust size of node, pivot
                    total_size = node.size
                    node.size -= pivot.left.size + 1
                    pivot.size = total_size

                # type Z                
                else:
                    pivot = node.left.right
                    side = node.left
                    node.left = None
                    side.right = None
                    pivot.right = node
                    pivot.left = side
                    # adjist size of node, pivot, side
                    total_size = node.size
                    node.size -= side.size
                    side.size -= pivot.size
                    pivot.size = total_size
            return pivot

        def remove(node, val, cnt=1):
            if not node:
                return
            
            if node.val == val:
                if node.cnt > cnt:
                    node.cnt -= cnt
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
            
            # size ignore duplicate vals
            node.size -= 1
            return node

        def successor(node) -> tuple[int]:
            node = node.right
            while node.left:
                node = node.left
            return node.val, node.cnt

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
            root, _ = add(root, vi)
            # print(f"i={i}")
            d = mindiff(root, vi)
            # print(f"d={d}")
            if d <= valueDiff:
                return True
        return False

class TreeNode:
    def __init__(self, val=None, left=None, right=None, cnt=1, size=1):
        self.val = val
        self.left = left
        self.right = right
        # duplicate val
        self.cnt = cnt
        # subtree size include curr node
        self.size = size