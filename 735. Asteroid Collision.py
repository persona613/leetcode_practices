"""
101 ms runtime beats 93.74%
17.5 MB memory beats 84.31%
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for ast in asteroids:
            while res and res[-1]>0 and ast<0:
                if res[-1] > abs(ast):
                    ast = 0
                    break
                elif res[-1] == abs(ast):
                    res.pop()
                    ast = 0
                    break
                else:
                    res.pop()
            if ast != 0:
                res.append(ast)
            # print(res)
        return res                      