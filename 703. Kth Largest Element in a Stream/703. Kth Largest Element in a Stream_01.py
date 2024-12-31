"""
Submission Result: Time Limit Exceeded
"""
class TreeNode:
    def __init__(self, val, cnt=1):
        self.val = val
        self.cnt = cnt
        self.left = None
        self.right = None

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        for n in nums:
            self.root = self.addnode(self.root, n)
        # res = []
        # def order(root):
        #     if not root:
        #         return
        #     order(root.left)
        #     res.append([root.val,root.cnt])
        #     order(root.right)
        # order(self.root)
        # print(res)
        
    def addnode(self, root, n):
        if not root:
            return TreeNode(n)
        elif root.val == n:
            pass
        elif n > root.val:
            root.right = self.addnode(root.right, n)
        else:
            root.left = self.addnode(root.left, n)
        root.cnt += 1
        return root
            
    def add(self, val: int) -> int:
        self.root = self.addnode(self.root, val)
        return self.findk(self.root, self.k).val
    
    def findk(self, root, k):
        if root.right:
            min_k = root.right.cnt + 1
        else:
            min_k = 1
        if root.left:
            max_k = root.cnt - root.left.cnt
        else:
            max_k = root.cnt
        
        if min_k <= k and k <= max_k:
            return root
        elif k < min_k:
            ret = self.findk(root.right, k)
        elif k > max_k:
            ret = self.findk(root.left, k-max_k)            
        return ret
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)