"""
164 ms runtime beats 84.11%
17.60 MB memory beats 24.97%
"""
class MyCalendar:

    def __init__(self):
        # dummy root
        self.root = Node(0, 0)

    def book(self, start: int, end: int) -> bool:
        return self.find(self.root, start, end)

    def find(self, root, start, end):
        if start >= root.end:
            if root.right is None:
                root.right = Node(start, end)
                return True
            return self.find(root.right, start, end)

        elif end <= root.start:
            if root.left is None:
                root.left = Node(start, end)
                return True
            return self.find(root.left, start, end)            
        return False
        

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)