"""
66 ms runtime beats 94.56%
19.97 MB memory beats 39.60%
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        res = []
        newhead = None
        head, tail = newInterval
        for i in range(len(intervals)):
            st_i, nd_i = intervals[i]
            if newhead == None:
                if nd_i < head:
                    res.append(intervals[i])
                    continue
                else:
                    newhead = min(st_i, head)
            if nd_i < tail:
                continue
            elif nd_i == tail:
                res.append((newhead, nd_i))
                res.extend(intervals[i + 1:])
                break
            else:
                if st_i > tail:
                    res.append((newhead, tail))
                    res.extend(intervals[i:])
                    break
                else:
                    res.append((newhead, nd_i))
                    res.extend(intervals[i + 1:])
                    break
        else:
            if newhead == None:
                return intervals + [newInterval]
            else:
                res.append((newhead, tail))
        return res
