"""
71 ms runtime beats 5.17%
16.37 MB memory beats 96.88%
"""
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for t, s in zip(seats, students):
            ans += abs(t - s)
        return ans