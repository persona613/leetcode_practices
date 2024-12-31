"""
1903 ms runtime beats 55.38%
29.23 MB memory beats 9.31%
"""
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [["."] * n for _ in range(m)]
        # move stones to right
        for i in range(m):
            # write and read
            w = n - 1
            for r in range(n - 1, -1, -1):
                # obstacle, jump write pointer to r - 1
                if box[i][r] == "*":
                    res[i][r] = "*"
                    w = r - 1
                # stone
                elif box[i][r] == "#":
                    res[i][w] = "#"
                    w -= 1
        return [row[::-1] for row in zip(*res)]