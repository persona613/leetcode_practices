"""
286 ms runtime beats 55.22%
23.10 MB memory beats 98.64%
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = defaultdict(set)
        for x, y in obstacles:
            obs[x].add(y)

        # N-E-S-W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # curr direction, curr x, curr y, max distance
        cd = cx = cy = mx = 0
        for command in commands:
            if command == -2:
                cd = (cd - 1) % 4
            elif command == -1:
                cd = (cd + 1) % 4
            else:
                dx, dy = dirs[cd]
                for _ in range(command):
                    nx = cx + dx
                    ny = cy + dy
                    if ny in obs[nx]:
                        break
                    cx = nx
                    cy = ny
                dist = cx ** 2 + cy ** 2
                mx = max(mx, dist)
        return mx
