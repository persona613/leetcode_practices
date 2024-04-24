"""
48 ms runtime beats 11.45%
16.59 MB memory beats 59.90%
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        s = deque(students)
        d = deque(sandwiches)
        tk = check = 0
        while s or d:
            if s[0] == d[0]:
                s.popleft()
                d.popleft()
                tk += 1
                check = 0
            else:
                s.append(s.popleft())
                check += 1
                if check == len(s):
                    break
        return n - tk