"""
47 ms runtime beats 86.72%
16.6 MB memory beats 9.53%
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        board = []
        for op in operations:
            if op == "+":
                board.append(board[-1] + board[-2])
            elif op == "D":
                board.append(board[-1] * 2)
            elif op == "C":
                board.pop()
            else:
                board.append(int(op))
        return sum(board)