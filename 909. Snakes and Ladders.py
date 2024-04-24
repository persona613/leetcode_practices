"""
100 ms runtime beats 70.07%
16.91 MB memory beats 55.45%
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def decode(k):
            i = (n - 1) - (k - 1) // n
            if n % 2 == 0:
                if i % 2 == 0: # reverse j at even row
                    j = (n - 1) - (k - 1) % n
                else:
                    j = (k - 1) % n
            else:
                if i % 2 == 0:
                    j = (k - 1) % n
                else: # reverse j at odd row
                    j = (n - 1) - (k - 1) % n
            return i, j

        n = len(board)
        ip = dict()
        for k in range(1, n **2 + 1):
            ip[k] = decode(k)

        seen = {1}
        q = deque([(1, 0)]) # (num, path)
        while q:
            curr, p = q.popleft()
            if curr == n ** 2:
                return p
            if p >= n ** 2:
                break
            for k in range(curr + 1, min(curr + 6, n ** 2) + 1):
                if k not in seen:
                    i, j = ip[k]
                    if board[i][j] == -1:
                        seen.add(k)
                        q.append((k, p + 1))

                    # if jump node, not add in seen
                    else:
                        nk = board[i][j]
                        if nk not in seen:
                            ni, nj = ip[nk]
                            if board[ni][nj] == -1:
                                seen.add(nk)
                            q.append((nk, p + 1))
        return -1