"""
Wrong Answer
20 / 25 testcases passed

Editorial
Input
slots1 =
[[10,60]]
slots2 =
[[12,17],[21,50]]
duration =
8

Use Testcase
Output
[]
Expected
[21,29]
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m = len(slots1)
        n = len(slots2)
        res = []
        i = j = 0
        # slots1 is bigger
        while i < m and j < n:
            a = slots1[i]
            b = slots2[j]
            if a[0] >= b[0]:
                end = min(a[1], b[1])
                if end - a[0] >= duration:
                    res.append([a[0], a[0] + duration])
                    break
                j += 1
            else:
                i += 1

        i = j = 0
        # slots2 is bigger
        while i < m and j < n:
            a = slots1[i]
            b = slots2[j]
            if b[0] >= a[0]:
                end = min(a[1], b[1])
                if end - b[0] >= duration:
                    res.append([b[0], b[0] + duration])
                    break
                i += 1
            else:
                j += 1

        if len(res) < 2:
            return res[0] if res else []
        return res[0] if res[0][0] <= res[1][0] else res[1]