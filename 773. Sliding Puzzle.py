"""
8 ms runtime beats 55.03%
16.87 MB memory beats 27.27%
"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # cells' adjs
        g = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        # {solvable states: steps}
        states_seen = dict()
        step = 0
        # (state-code: tuple, zero-index)
        q = deque([((1,2,3,4,5,0), 5)])
        while q:
            ln = len(q)
            for _ in range(ln):
                curr, zero_pos = q.popleft()
                if curr in states_seen:
                    continue
                states_seen[curr] = step

                for adj in g[zero_pos]:
                    arr = list(curr)
                    arr[zero_pos], arr[adj] = arr[adj], arr[zero_pos]
                    q.append((tuple(arr), adj))
            step += 1
        b = tuple(board[0] + board[1])
        return states_seen.get(b, -1)
        