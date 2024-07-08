"""
159 ms runtime beats 71.12%
18.40 MB memory beats 50.76%
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1:
            return True
            
        # cnt dict
        dic = dict()
        for h in hand:
            dic[h] = dic.get(h, 0) + 1

        keys = sorted(dic.keys(), reverse = True)
        while dic:
            while keys[-1] not in dic:
                keys.pop()
            st = keys[-1]
            for v in range(st, st + groupSize):
                if v in dic:
                    dic[v] -= 1
                    if dic[v] == 0:
                        del dic[v]
                else:
                    return False
        return True