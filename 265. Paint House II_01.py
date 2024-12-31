"""
3 ms runtime beats 98.48%
16.70 MB memory beats 69.07%
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        # find 2 min cost and min cost index
        pre_cost1 = pre_cost2 = pre_color = None
        for color, cost in enumerate(costs[0]):
            if pre_cost1 is None or cost < pre_cost1:
                pre_cost2 = pre_cost1
                pre_cost1 = cost
                pre_color = color
            elif pre_cost2 is None or cost < pre_cost2:
                pre_cost2 = cost
        
        for i in range(1, n):
            # curr 2 min cost and min cost index
            cost1 = cost2 = curr_color = None
            for color in range(k):
                # update with pre 2 min cost
                cost = costs[i][color]
                if color == pre_color:
                    cost += pre_cost2
                else:
                    cost += pre_cost1
                
                # compare curr row
                if cost1 is None or cost < cost1:
                    cost2 = cost1
                    cost1 = cost
                    curr_color = color
                elif cost2 is None or cost < cost2:
                    cost2 = cost

            pre_cost1 = cost1
            pre_cost2 = cost2
            pre_color = curr_color
        return pre_cost1