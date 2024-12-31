"""
Time Limit Exceeded
22 / 25 testcases passed
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m = len(slots1)
        n = len(slots2)
        for i in range(m):
            a = slots1[i]
            for j in range(n):
                b = slots2[j]
                if a[0] > b[1]:
                    continue
                elif b[0] > a[1]:
                    break
                else:
                    start = max(a[0], b[0])
                    end = min(a[1], b[1])
                    if end - start >= duration:
                        return [start, start + duration]
        return []