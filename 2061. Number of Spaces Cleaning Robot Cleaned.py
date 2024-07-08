"""
313 ms runtime beats 81.71%
19.65 MB memory beats 20.73%
"""
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def move(i, j, head, cleaned):
            if (i, j) in seen:
                if seen[(i, j)] == head:
                    return cleaned
            else:
                cleaned += 1
            seen[(i, j)] = head

            ni = i + dirs[head][0]
            nj = j + dirs[head][1]
            # turn head or not
            for _ in range(4):
                if not valid(ni, nj) or room[ni][nj] == 1:
                    head = (head + 1) % 4
                    ni = i + dirs[head][0]
                    nj = j + dirs[head][1]
                else:
                    return move(ni, nj, head, cleaned)
            return cleaned

        # 0:right, 1:down, 2:left, 3:up
        dirs = {0: (0, 1), 1: (1, 0), 2:(0, -1), 3:(-1, 0)}
        m = len(room)
        n = len(room[0])
        # seen = defaultdict(lambda: -1)
        seen = dict()
        return move(0, 0, 0, 0)