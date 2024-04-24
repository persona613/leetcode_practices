"""
41 ms runtime beats 83.79%
16.86 MB memory beats 36.98%
"""
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        arr = sorted(deck)
        res = deque([arr.pop()])
        while arr:
            res.appendleft(res.pop())
            res.appendleft(arr.pop())
        return res