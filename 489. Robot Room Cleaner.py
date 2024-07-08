"""
47 ms runtime beats 86.04%
17.71 MB memory beats 6.17%
"""
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # face={0:up, 1:right, 2:down, 3:left}
        def dfs(i, j, face, backway):
            robot.clean()
            for w in range(face, face + 4):
                if w - face > 0:
                    robot.turnRight()
                di, dj = dirs[w % 4]
                ni, nj = i + di, j + dj
                if (ni, nj) not in seen:
                    seen.add((ni, nj))
                    if robot.move():
                        dfs(ni, nj, w % 4, (w + 2) % 4)
                        # after robot turn back, restore origin face-way
                        robot.turnRight()
                        robot.turnRight()
            robot.turnLeft()
            robot.move()
        
        dirs = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
        seen = {(0, 0)}
        dfs(0, 0, 0, None)