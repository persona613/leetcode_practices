"""
65 ms runtime beats 43.76%
20 MB memory beats 64.31%
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque()
        for nst in nestedList:
            self.dfs(nst)
        # print(self.q)

    def next(self) -> int:
        return self.q.popleft()
    
    def hasNext(self) -> bool:
         if self.q:
             return True
         else:
             return False

    def dfs(self, nst):        
        if nst.isInteger():
            self.q.append(nst.getInteger())
        else:
            lst = nst.getList()
            for a in lst:
                self.dfs(a)



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())