"""
Time Limit Exceeded
48 / 52 testcases passed
submitted at May 03, 2024 22:45

indexDiff =
100000
valueDiff =
0
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def add(node, val):
            if not node:
                return TreeNode(val)

            if node.val == val:
                node.cnt += 1
            elif node.val < val:
                node.right = add(node.right, val)
            else:
                node.left = add(node.left, val)
            return node

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

            if node.val < val:
                node.right = remove(node.right, val)
            else:
                node.left = remove(node.left, val)
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
            add(root, vi)
            # print(f"i={i}")
            d = mindiff(root, vi)
            # print(f"d={d}")
            if d <= valueDiff:
                return True
        return False

class TreeNode:
    def __init__(self, val=None, left=None, right=None, cnt=1):
        self.val = val
        self.left = left
        self.right = right
        self.cnt = cnt