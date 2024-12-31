"""
1191 ms runtime beats 33.33%
56.38 MB memory beats 49.16%
"""
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # line sweep
        timeline = []
        for interval in intervals:
            timeline.append((interval[0], 1))
            timeline.append((interval[1] + 1, -1))
        timeline.sort()

        # overlap interval
        overlap = 0
        mx = 0
        for event in timeline:
            overlap += event[1]
            if overlap > mx:
                mx = overlap
        return mx 