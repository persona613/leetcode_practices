"""
811 ms runtime beats 30.10%
18.7 MB memory beats 18.91%
"""
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat_num = len(candyType) // 2
        type_num = len(set(candyType))
        if type_num <= eat_num:
            return type_num
        return eat_num