"""
470 ms runtime beats 27.49%
24.24 MB memory beats 50.00%
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m = len(slots1)
        n = len(slots2)
        res = []
        i = j = 0
        # assume slots1 is bigger
        while i < m and j < n:
            a = slots1[i]
            b = slots2[j]
            if a[0] > b[1]:
                j += 1
            elif b[0] > a[1]:
                i += 1
            else:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                if end - start >= duration:
                    res.append([start, start + duration])
                    break
                else:
                    # assume slots1 is bigger
                    j += 1

        i = j = 0
        # assume slots2 is bigger
        while i < m and j < n:
            a = slots1[i]
            b = slots2[j]
            if a[0] > b[1]:
                j += 1
            elif b[0] > a[1]:
                i += 1
            else:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                if end - start >= duration:
                    res.append([start, start + duration])
                    break
                else:
                    # assume slots2 is bigger
                    i += 1

        if len(res) < 2:
            return res[0] if res else []
        return res[0] if res[0][0] <= res[1][0] else res[1]