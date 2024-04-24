"""
39 ms runtime beats 53.82%
16.88 MB memory beats 72.90%
"""
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        for i in range(1, len(currentState)):
            if currentState[i] == "+" \
                and currentState[i-1] == "+":

                res.append("".join([currentState[:i-1], \
                    "--", currentState[i+1:]]))
        return res
