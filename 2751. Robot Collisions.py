"""
997 ms runtime beats 50.00%
43.66 MB memory beats 55.77%
"""
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(set(directions)) == 1:
            return healths
        
        robots = zip(positions, healths, directions, range(len(positions)))
        robots = [list(tup) for tup in robots]
        robots.sort()

        stk = []
        for robot in robots:
            while stk and stk[-1][2] == "R" and robot[2] == "L":
                if stk[-1][1] < robot[1]:
                    robot[1] -= 1
                    stk.pop()
                else:
                    if stk[-1][1] > robot[1]:
                        stk[-1][1] -= 1
                    # equal health
                    else:
                        stk.pop()
                    break
            else:
                stk.append(robot)
            
        # restore origin order
        stk.sort(key = lambda x: x[3])
        return [robot[1] for robot in stk]