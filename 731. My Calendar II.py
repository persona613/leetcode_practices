"""
1108 ms runtime beats 39.58%
18.07 MB memory beats 7.51%
"""
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.books = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.books[start] = self.books.get(start, 0) + 1
        self.books[end] = self.books.get(end, 0) - 1
        cnt = 0
        for time in self.books:
            cnt += self.books[time]
            if cnt >= 3:
                self.books[start] -= 1
                self.books[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)