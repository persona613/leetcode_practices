"""
979 ms runtime beats 65.73%
35.57 MB memory beats 91.28%
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        q = [(nums1[0] + nums2[0], 0, 0)]
        seen = {(0, 0)}
        for _ in range(k):
            val, i, j = heapq.heappop(q)
            res.append((nums1[i], nums2[j]))
            if i + 1 < n1 and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(q, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < n2 and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
        return res