"""
787 ms runtime beats 82.91%
30.24 MB memory beats 47.86%
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def check_force(w, n):
            curr_idx = 0
            curr = position[0]
            # find m-2 points
            # exclude first and last points
            # they must be at 0 and n-1 index
            for _ in range(m - 2):
                nxt = curr + w
                nxt_idx = bisect_left(position, nxt, curr_idx + 1, n - 1)
                # chect new interval
                # if nxt_idx >= n or position[nxt_idx] - curr < w:
                if nxt_idx >= n or nxt_idx <= curr_idx:
                    return False
                curr_idx = nxt_idx
                curr = position[nxt_idx]

            # after cutting m-2 middle points, check last interval
            return position[-1] - curr >= w

        if m == 2:
            return max(position) - min(position)

        position.sort()
        n = len(position)
        if m == n:
            return min(a - b for a, b in zip(position[1:], position))

        # r: max force
        r = (position[-1] - position[0]) // (m - 1)
        l = 1
        while l < r:
            # right-index-mid
            mid = (l + r) // 2 + 1
            if check_force(mid, n):
                l = mid
            else:
                r = mid - 1
        return l