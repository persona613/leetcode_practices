"""
795 ms runtime beats 13.06%
57.20 MB memory beats 45.36%
"""
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = sum(customers[0])
        # running time
        rt = customers[0][1]
        for arrive, prepare in customers[1:]:
            # starts preparing time + preparation
            # if curr >= arrive:
            #     rt += curr - arrive + prepare
            #     curr = curr + prepare
            # else:
            #     rt += prepare
            #     curr = arrive + prepare

            rt += max(curr - arrive, 0) + prepare
            curr = max(curr, arrive) + prepare
        return rt / len(customers) 
            